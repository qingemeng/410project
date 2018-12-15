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
from flask import Flask, request, jsonify, render_template
from search_engine import init_search_engine

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
    results = []
    idxs, dists = se.search(query)
    ranked_results = sorted(zip(idxs, dists), key=lambda input: rank(input, ref_df))
    for idx, dist in ranked_results[:10]:
        content = ref_df.iloc[idx].content
        url = ref_df.iloc[idx].url
        vote = ref_df.iloc[idx].vote
        polarity = ref_df.iloc[idx].sentiment_polarity
        subjectivity = ref_df.iloc[idx].sentiment_subjectivity
        score = dist + 0.01 / vote + 0.001 / polarity
        results.append({'content': content, 'score': score, 'url': url})
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
    query_string = request.args.get('query_string')
    if not query_string:
        render_template('index.html')
    results = search(search_engine, ref_df, query_string)
    # return render_template('index.html', text=request.form['text'])
    return jsonify(results)

if __name__ == '__main__':
    ref_df, search_engine = init_search_engine()
    app.run(port=5001, host='0.0.0.0')
