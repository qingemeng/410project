# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_python37_app]
from flask import Flask, request, render_template_string, url_for
from search_engine import init_search_engine
from json2html import *

app = Flask(__name__)
ref_df = 'global'
search_engine = 'global'


def rank(input, ref_df):
    idx, dist = input
    vote = ref_df.iloc[idx].vote
    polarity = ref_df.iloc[idx].sentiment_polarity
    subjectivity = ref_df.iloc[idx].sentiment_subjectivity
    return dist + 0.01 / vote + 0.001 / polarity


def search(se, ref_df, query):
    results = ""
    idxs, dists = se.search(query)
    ranked_results = sorted(zip(idxs, dists), key=lambda input: rank(input, ref_df))
    for idx, dist in ranked_results[:100]:
        content = ref_df.iloc[idx].content
        url = ref_df.iloc[idx].url
        vote = ref_df.iloc[idx].vote
        polarity = ref_df.iloc[idx].sentiment_polarity
        subjectivity = ref_df.iloc[idx].sentiment_subjectivity
        score = dist + 0.01 / vote + 0.001 / polarity
        results = results + f'{content}<br>'
        results = results +f'score: {round(score, 6)}<br>'
        results = results + f'url: <a href="{url}">{url}</a><br>'
        results = results + '<p>---------------</p>'
        
        print(content)
        print(f'score: {score}')
        print(f'url: {url}\n---------------\n')

    return results


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World!!!'


@app.route('/search')
def retrieve():
    query_string = request.args.get('query')
    results = ''
    if query_string:
        results = search(search_engine, ref_df, query_string)


    search_template = '''
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
            <link rel=stylesheet type=text/css href="{css_file}">
        </head>
        <body>   
            <div class="content">
                <form method="get" action="/search">
                    <input type="text" name="query">
                    <input type="submit">
                </form>
                {results}
            </div>
        </body>
        </html>
        '''.format(results=results, css_file= url_for('static', filename='style.css'))
    return render_template_string(search_template)


if __name__ == '__main__':
    ref_df, search_engine = init_search_engine()
    app.run(port=5001, host='0.0.0.0')
