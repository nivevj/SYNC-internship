from flask import Flask, render_template, request
import pyshorteners

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/shorten', methods=['POST'])
def hello():
    url=request.form['link']
    shortener=pyshorteners.Shortener()
    short_url=shortener.tinyurl.short(url)
    print(short_url)
    return render_template('home.html',var=short_url)


if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 3000,debug=True)
    