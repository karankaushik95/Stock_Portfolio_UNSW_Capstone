from flask import render_template, request, redirect, url_for
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user 
from server import app, login_service
from modules.stock.stock_m_worker import stockMWorker
from modules.stock.stock_s_worker import stockSWorker
from modules.search.search_s_worker import searchSWorker
from service.login.login_service import User
import json
import requests


@app.route('/api')
def test_api():
    url = app.config["IEX_SANDBOX_URL"] + "stock/AAPL/quote" + app.config["IEX_SANDBOX_TOKEN"]
    data = requests.get(url)
    json_data = json.loads(data.text)
    return json.dumps(json_data)

@app.route('/index.html', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['username']
        password = request.form['password']
        if (login_service.check(email,password)):
            user = User(email)
            login_service.login_session_user(user)
            login_user(user)
            return json.dumps({"success":"true"})
        else:
            return json.dumps({"success":"false"})
    return render_template('error.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST': 
        name = request.form['registerName']
        email = request.form['registerUsername']
        password = request.form['registerPassword']
        if (login_service.user_exists(email)):
            return json.dumps({"success":"false"})
        else:
            login_service.new_user(name, email, password)
            return json.dumps({"success":"true"})
    return "404"

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

@app.route('/login.html')
def work():
    return render_template('login.html')


@app.route('/dashboard.html')
@login_required
def dashboard():
    return render_template('dashboard.html')


# SHARE PROFILE ROUTE NO HTML YET
# USES APLHAVANTAGE
# THE INTERVAL SHOULD BE SETTABLE ON THE PAGE
# SAME WITH TYPE OF SERIES, (ADJUSTED/NOT ADJUSTED) AND TIME FRAME
@app.route('/stock/<ticker>')
def stock_info(ticker):
    quote_data = stockSWorker.av_quote(ticker)
    stockMWorker.av_tidy_quote(quote_data)

    # ---- THESE FUNCTIONS MAKE THE LOADING QUITE SLOW ---- NEED TO OPTIMISE SOMEHOW
    # shareMWorker.av_market_cap(quote_data)
    # shareMWorker.av_daily_range(quote_data, ticker)
    # shareMWorker.av_52_high_low(quote_data, ticker)

    interval = '60min'
    series = 'DAILY'
    adj_flag = True
    time_series = stockSWorker.av_time_series(ticker, interval, series, adj_flag)
    json_data = stockMWorker.av_create_json(quote_data, time_series)
    return json.dumps(json_data)


# SHARE PROFILE ROUTE NO HTML YET
# USES APLHAVANTAGE
# THE INTERVAL SHOULD BE SETTABLE ON THE PAGE
# SAME WITH TYPE OF SERIES, (ADJUSTED/NOT ADJUSTED) AND TIME FRAME
@app.route('/market/<mticker>')
def market_info(mticker):
    indices = []

    # WE CAN ADD MORE INDICES BUT IT MAKES THE LOADING VERY SLOW
    # NEED TO INVESTIGATE MULTIPROCESSING
    # NEEDS ERROR CHECKING AS WELL
    if mticker == 'NASDAQ':
        indices = ['INX']
    elif mticker == 'NYSE':
        indices = ['NYA']
    else:
        redirect(url_for(error))

    quotes = {}
    for index in indices:
        quote_data = stockSWorker.av_quote(index)
        stockMWorker.av_tidy_quote(quote_data)

        # ---- THESE FUNCTIONS MAKE THE LOADING QUITE SLOW ---- NEED TO OPTIMISE SOMEHOW
        # shareMWorker.av_market_cap(quote_data)
        # shareMWorker.av_daily_range(quote_data, ticker)
        # shareMWorker.av_52_high_low(quote_data, ticker)

        interval = '60min'
        series = 'DAILY'
        adj_flag = True
        time_series = stockSWorker.av_time_series(index, interval, series, adj_flag)
        json_data = stockMWorker.av_create_json(quote_data, time_series)
        quotes[index] = (json_data)

    return json.dumps(quotes)


# PRODUCES THE SEARCH RESULTS, MIGHT NOT NEED TO BE ITS OWN ROUTE BUT HEY
@app.route('/search', methods=['GET', 'POST'])
def security():
    if request.method == 'POST':
        search = request.form['search']
        json_data = searchSWorker.av_search_string(search)
        return json.dumps(json_data)
    return None


@app.route('/test')
def test_symbols():
    url = app.config["IEX_CLOUD_URL"] + "ref-data/symbols" + app.config["IEX_CLOUD_TOKEN"]
    data = requests.get(url)
    json_data = json.loads(data.text)
    return json.dumps(json_data)


@app.route('/error')
def error():
    return "404"

