from flask import Flask, render_template, redirect, request
from helpers.helper import execute_apple, execute_techcrunch


# define flask app
# and configure
app = Flask(__name__)


@app.route('/')
def index():
    news_sources_api_calls = ['Apple News', 'Techcrunch', 'The San Francisco Chronicle']
    return render_template('index.html', news_source=news_sources_api_calls)


@app.route('/news_source/<news>', methods=["GET"])
def get_news_source(news):

    # TODO: This line of code should instead direct user
    # to the respective news webpage
    # perhaps most recent article

    # for now, the user cannot choose their news source dynamically.
    # edit: will use a different api which gets various
    # news sources based on keyword search by user - Bingo
    # Use another page on app which allows THIS
    

    # TODO: maybe define multiple functions above to
    # access these APIs, which are all different.
    # Research Atlantic + Bloomberg apis ~~DONE~~

    apple_api_call = execute_apple()
    atlantic_api_call = execute_techcrunch()
    # bloomberg = execute_bloom()
    return redirect(apple_api_call)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)