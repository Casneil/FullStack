# project/main/views.py

from flask import render_template, Blueprint, redirect, url_for, jsonify
from forms import SearchForm
import json
import requests

main_blueprint = Blueprint('main', __name__, )


@main_blueprint.route('/', methods=('GET', 'POST'))
def search():
    form = SearchForm()
    if form.validate_on_submit():
        return search_results(form.searchterm.data)

    return render_template('main/index.html', form=form)


@main_blueprint.route("/results")
def search_results(search_query):
    return render_template('main/results.html', results=None,
                           query=search_query)



def query_API(searchterm):from flask import Flask, render_template, request
tenor_apikey = 	"XXL60F3ZPTI9"
    r = requests.get('https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s&anon_id=%s' % (search_query, tenor_apikey))
    if r.status_code == 200:
        top_8gifs = json.loads (r.content)
        print (top_8gifs)

    else:
        top_8gifs = none    
    # return tenor_apikey
        # return search_query

