from flask import Flask, render_template
import requests

# to easily generate an api call response
def execute_nyt():
    requestUrl = "https://api.nytimes.com/svc/mostpopular/v2/viewed/1.json?api-key=6CIcTlf5BAmG5u4ttYxeOGAFlAWJhXFr"
    requestHeaders = {
    "Accept": "application/json"
  }
    response = requests.get(requestUrl, headers=requestHeaders)
    return response.text
  

app = Flask(__name__)


@app.route('/')
def index():
    news_sources_api_calls = ['The New York Times', 'The Atlantic', 'The San Francisco Chronicle']
    return render_template('index.html', news_source=news_sources_api_calls)


@app.route('/news_source/<news>')
def get_news_source(news):

    # TODO: This line of code should instead direct user
    # to the respective news webpage
    # perhaps most recent article

    # for now, the user cannot choose their news source dynamically.
    # Will need a web scraping tool or something to get this.
    # for now, will allow user three options. For MVP...

    # https://developer.nytimes.com/apis - ny times api page
    

    
    nyt_response = execute_nyt()
    atlantic_api_call = '#'
    sf_api_call = '#'
    return nyt_response["results"]  # this doesn't work yet. Not subscriptable.

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)