# main.py

from app import app
from db_setup import init_db, db_session
from forms import CodeSearchForm
from flask import flash, render_template, request, redirect
from models import so_code

init_db()


@app.route('/', methods=['GET', 'POST'])
def index():
    search = CodeSearchForm(request.form)
    if request.method == 'POST':
        return search_results(search)

    return render_template('index.html', form=search)


@app.route('/results')
def search_results(search):
    results = []
    search_string = search.data['search']

    if search.data['search'] == '':
        qry = db_session.query(so_code)
        results = qry.all()

    if not results:
        flash('No results found!')
        return redirect('/')
    else:
        # display results
        return render_template('results.html', table=table)

if __name__ == '__main__':
    import os
    if 'WINGDB_ACTIVE' in os.environ:
        app.debug = False
    app.run(port=5001)