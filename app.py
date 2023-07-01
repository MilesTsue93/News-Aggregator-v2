from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    news_sources = ['The New York Times', 'The Atlantic', 'The San Francisco Chronicle']
    return render_template('index.html')


@app.route('/news/<news>')
def news(news):
    return 'This is ' + str(news)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)