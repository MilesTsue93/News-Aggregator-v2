from flask import Flask, render_template, redirect, request
from dotenv import load_dotenv
from flask_mail import Mail, Message 
from serpapi import GoogleSearch
from config import mail_username, mail_password
import os
import json
import requests

# for api keys
def load_api_keys():
    load_dotenv()


def execute_nyt():

    '''
    nytimes function returns top article
    '''

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

    ''' 
    returns top google news article based on user query.
    TODO: right now 'hamas' is hardcoded as the user query.
    Find a way to dynamically allow user to query
    '''
    load_api_keys()
    params = {
    "q": "hamas",
    "hl": "en",
    "gl": "us",
    "api_key":  os.getenv("SERAPI_API_KEY")
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    top_stories = results["top_stories"]
    return top_stories[1]["link"]

# define flask application
app = Flask(__name__)

# configurations for contact us page
app.config["MAIL_SERVER"] = "smtp.office365.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USE_SSL"] = False
app.config["MAIL_USERNAME"] = mail_username
app.config["MAIL_PASSWORD"] = mail_password
mail = Mail(app)


@app.route('/')
def index():
    news_sources_api_calls = ['The New York Times', 'Google News']
    return render_template('index.html', news_source=news_sources_api_calls)


@app.route('/news_source/<news>', methods=["GET"])
def get_news_source(news):

    # TODO: Create a webscraping script to embed the news 
    # articles scraped from the web into the app page!

    nyt_response = execute_nyt()
    google_news = execute_google_news()

    if news == "The New York Times":
        return redirect(nyt_response)
    elif news == "Google News":
        return redirect(google_news)


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