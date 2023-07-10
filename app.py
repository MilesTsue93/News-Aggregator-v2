from flask import Flask, render_template, redirect, request
from helper import read_config, execute_nyt#, execute_bloom


# define flask app
# and configure
app = Flask(__name__)
config = read_config()
API_KEY = config["FTPSettings"]["api_key"]


@app.route('/')
def index():
    news_sources_api_calls = ['The New York Times', 'The Atlantic', 'The San Francisco Chronicle']
    return render_template('index.html', news_source=news_sources_api_calls)


@app.route('/news_source/<news>', methods=["GET"])
def get_news_source(news):

    # TODO: This line of code should instead direct user
    # to the respective news webpage
    # perhaps most recent article

    # for now, the user cannot choose their news source dynamically.
    # Will need a web scraping tool or something to get this.
    # for now, will allow user three options. For MVP...

    # https://developer.nytimes.com/apis - NYTimes api page
    

    # TODO: maybe define multiple functions above to
    # access these APIs, which are all different.
    # Research Atlantic + Bloomberg apis

    # link to docs on bloomberg apis: 
    # https://bloomberg.github.io/blpapi-docs/python/3.20/

    nyt_response = execute_nyt()
    atlantic_api_call = '#'
    bloomberg = '#'
    return redirect(nyt_response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)