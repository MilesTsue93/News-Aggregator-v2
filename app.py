from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    news_sources = ['The New York Times', 'The Atlantic', 'The San Francisco Chronicle']
    return render_template('index.html', news_source=news_sources)


@app.route('/news_source/<news>')
def news_source(news):

    # TODO: This line of code should instead direct user
    #  to the respectivenews webpage
    # perhaps most recent article

    # for now, the user cannot choose their news source dynamically.
    # Will need a web scraping tool or something to get this.
    # for now, will allow user three options. For MVP...

    # https://developer.nytimes.com/apis - ny times api page
    nyt_api_call = 'https://api.nytimes.com/svc/mostpopular/v2/viewed/1.json?api-key={6CIcTlf5BAmG5u4ttYxeOGAFlAWJhXFr}'
    atlantic_api_call = '#'
    sf_api_call = '#'
    match news:
        case 'The New York Times':
            return nyt_api_call
        case 'The Atlantic':
            return atlantic_api_call
        case 'The San Francisco Chronicle':
            return sf_api_call 
    return 


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)