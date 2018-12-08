# main.py

from app import app
#from db_setup import init_db, db_session
from forms import CodeSearchForm
from flask import flash, render_template, request, redirect
import sesearch as se 
import json


@app.route('/', methods=['GET', 'POST'])
def index():
    search = CodeSearchForm(request.form)
    if request.method == 'POST':
        return search_results(search)

    return render_template('index.html', form=search)


@app.route('/results')
def search_results(search):
    results = {}
    search_string = search.data['search']
    results = se.se_search(search_string)
# =============================================================================
#     if search.data['search'] == '':
#         qry = db_session.query(so_code)
#         results = qry.all()
# =============================================================================

    if not results:
        flash('No results found!')
        return redirect('/')
    else:
        
        return render_template('results.html', results=results)

if __name__ == '__main__':
    import os
    if 'WINGDB_ACTIVE' in os.environ:
        app.debug = True
    app.run(port=5001)
        
# =============================================================================
# if __name__ == '__main__':
#     app.run(debug=True)
# =============================================================================
