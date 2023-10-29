from flask import Flask, render_template, redirect, request
from dotenv import load_dotenv
import os

from serpapi import GoogleSearch

import json
import requests

# for api keys
def load_api_keys():
    load_dotenv()

# to easily generate an api call response
#  - may not need actually, might be more cumbersome!
def execute_nyt():
    load_api_keys()
    requestUrl = f"https://api.nytimes.com/svc/mostpopular/v2/viewed/1.json?api-key={os.getenv('NYT_API_KEY')}"
    requestHeaders = {
    "Accept": "application/json"
  }
    
    response = requests.get(requestUrl, headers=requestHeaders)
    
    # convert to json format
    response_dict = json.loads(response.text)

    print(response_dict["results"][0]["url"])
    return response_dict["results"][0]["url"]

def execute_google_news():

    load_api_keys()
    params = {
    "q": "trump",
    "hl": "en",
    "gl": "us",
    "api_key":  os.getenv("SERAPI_API_KEY")
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    top_stories = results["top_stories"]
    print(top_stories)
    return top_stories[0]

# define flask application
app = Flask(__name__)


@app.route('/')
def index():
    news_sources_api_calls = ['The New York Times', 'Google News', 'The San Francisco Chronicle']
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

    sources = []
    nyt_response = execute_nyt()
    google_news = execute_google_news()
    sf_api_call = '#'

    sources.append(nyt_response)
    sources.append(google_news)
    sources.append(sf_api_call)


    return redirect(nyt_response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)