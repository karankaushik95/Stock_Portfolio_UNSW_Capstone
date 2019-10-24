from flask import render_template, request, redirect, url_for
from server import app
import json
import requests


@app.route('/api')
def test_api():
    url = app.config["IEX_SANDBOX_URL"] + "stock/AAPL/quote" + app.config["IEX_SANDBOX_TOKEN"]
    data = requests.get(url)
    json_data = json.loads(data.text)
    return json.dumps(json_data)


@app.route('/index.html')
def index():
    return render_template('index.html')


@app.route('/about.html')
def about():
    return render_template('about.html')


@app.route('/blog-single.html')
def blog_single():
    return render_template('blog-single.html')


@app.route('/blog.html')
def blog():
    return render_template('blog.html')


@app.route('/contact.html')
def contact():
    return render_template('contact.html')


@app.route('/pricing.html')
def pricing():
    return render_template('pricing.html')


@app.route('/services.html')
def services():
    return render_template('services.html')


@app.route('/team.html')
def team():
    return render_template('team.html')


@app.route('/work.html')
def work():
    return render_template('work.html')


@app.route('/security/<ticker>.html')
def security_info(ticker):
    url = app.config["IEX_CLOUD_URL"] + "stock/{}/quote" + app.config["IEX_CLOUD_TOKEN"]
    url = url.format(ticker)
    print(url)
    data = requests.get(url)
    json_data = json.loads(data.text)
    return json.dumps(json_data)


@app.route('/security.html', methods=['GET', 'POST'])
def security():
    if request.method == 'POST':
        ticker = request.form['ticker']
        return redirect(url_for('security_info', ticker=ticker))
    return render_template('security.html')


@app.route('/test')
def test_symbols():
    url = app.config["IEX_CLOUD_URL"] + "ref-data/symbols" + app.config["IEX_CLOUD_TOKEN"]
    data = requests.get(url)
    json_data = json.loads(data.text)
    return json.dumps(json_data)
