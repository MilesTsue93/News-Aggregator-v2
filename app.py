from flask import Flask, render_template, redirect, request
from dotenv import load_dotenv
import os
from jinja2 import Template
import sqlalchemy
from flask_mail import Mail, Message 
from serpapi import GoogleSearch
from config import mail_username, mail_password

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
    #print(top_stories[1]["link"])
    return top_stories[1]["link"]

# define flask application
app = Flask(__name__)

# configurations
app.config["MAIL_SERVER"] = "smtp.office365.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USE_SSL"] = False
app.config["MAIL_USERNAME"] = mail_username
app.config["MAIL_PASSWORD"] = mail_password


mail = Mail(app)
#db = sqlalchemy(app)
#admin = Admin(app)

@app.route('/')
def index():
    news_sources_api_calls = ['The New York Times', 'Google News', 'The San Francisco Chronicle']
    return render_template('index.html', news_source=news_sources_api_calls)


@app.route('/news_source/<news>', methods=["GET"])
def get_news_source(news):

    # TODO: This line of code should instead direct user
    # to the respective news webpage
    # perhaps most recent article ~~DONE~~

    # for now, the user cannot choose their news source dynamically.
    # edit: will use a different api which gets various
    # news sources based on keyword search by user - Bingo
    # Use another page on app which allows THIS
    

    # TODO: maybe define multiple functions above to
    # access these APIs, which are all different.
    # Research Atlantic + Bloomberg apis ~~DONE~~

    nyt_response = execute_nyt()
    google_news = execute_google_news()
    sf_api_call = '#'

    if news == "The New York Times":
        return redirect(nyt_response)
    elif news == "Google News":
        return redirect(google_news)
    else:
        return news
    
@app.route('/contact.html', methods=["GET", "POST"])

def contact():
    if request.method == "GET":
        return render_template("contact.html")

    if request.method == "POST":
        firstname = request.form.get("firstname")
        lastname = request.form.get("lastname")
        country = request.form.get("country")
        message = request.form.get("message")

        msg = Message(
            subject=f"Mail from{firstname} {lastname}", body=f"from: {country}\n{firstname} writes:\n\n{message}",
            sender=mail_username, recipients=[mail_username]
        )
        mail.send(msg)
        return render_template("contact.html", success=True)
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)