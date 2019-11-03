from flask import render_template, request, redirect, url_for
from server import app
from modules.share.share_m_worker import shareMWorker
from modules.share.share_s_worker import shareSWorker
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


@app.route('/dashboard.html')
def dashboard():
    return render_template('dashboard.html')


# SHARE PROFILE ROUTE NO HTML YET
# USES APLHAVANTAGE
# THE INTERVAL SHOULD BE SETTABLE ON THE PAGE
# SAME WITH TYPE OF SERIES, (ADJUSTED?NOT ADJUSTED) AND TIME FRAME
@app.route('/security/<ticker>.html')
def security_info(ticker):
    quote_data = shareSWorker.av_quote(ticker)
    shareMWorker.av_tidy_quote(quote_data)

    # ---- THESE FUNCTIONS MAKE THE LOADING QUITE SLOW ---- NEED TO OPTIMISE SOMEHOW
    # shareMWorker.av_market_cap(quote_data)
    # shareMWorker.av_daily_range(quote_data, ticker)
    # shareMWorker.av_52_high_low(quote_data, ticker)

    interval = '60min'
    series = 'DAILY'
    adj_flag = True
    time_series = shareSWorker.av_time_series(ticker, interval, series, adj_flag)
    json_data = shareMWorker.av_create_json(quote_data, time_series)
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
