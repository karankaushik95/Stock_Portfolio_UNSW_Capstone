from flask import render_template, request, redirect, url_for, Response, flash
import flask_login
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user
from server import app, login_service
from modules.stock.stock_m_worker import stockMWorker
from modules.stock.stock_s_worker import stockSWorker
from modules.search.search_s_worker import searchSWorker
from user.user import User
import json
import requests


@app.route('/index.html', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/login.html', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    if request.method == 'POST':
        email = request.form['username']
        passwd = request.form['password']
        if login_service.check(email, passwd):
            print('here')
            user = User(email)
            login_service.login_session_user(user)
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            return Response(status="401")   
    return render_template('login.html')


@app.route('/logout')
def logout():
    login_service.login_session_user(current_user)
    logout_user()
    return redirect(url_for('index'))


@app.route('/signup.html', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    if request.method == 'POST':
        email = request.form['regemail']
        name = request.form['regname']
        password = request.form['regpassword']
        if (login_service.user_exists(email)):
            return Response(status="401")
        else:
            login_service.new_user(name, email, password)
            user = User(email)
            login_service.login_session_user(user)
            login_user(user)
            return redirect(url_for('dashboard'))
    return render_template('register.html')


# ENDPOINT FOR USER DATA
@app.route('/user_data')
@login_required
def user_data():
    return json.dumps(current_user.get_details())


# ENDPOINT FOR USER PORTFOLIOS
@app.route('/user_portfolios')
@login_required
def user_portfolios():
    return json.dumps(current_user.get_portfolios())


# ENDPOINT FOR USER WATCHLISTS
@app.route('/user_watchlist')
@login_required
def user_watchlists():
    return json.dumps(current_user.get_watchlist())


@app.route('/remove_watchlist_stock/<ticker>')
@login_required
def remove_watchlist_stock(ticker):
    current_user.remove_watchlist_stock(ticker)
    return redirect(url_for('user_watchlists'))


@app.route('/add_watchlist_stock/<ticker>')
@login_required
def add_watchlist_stock(ticker):
    current_user.add_watchlist_stock(ticker)
    return redirect(url_for('user_watchlists'))


@app.route('/remove_portfolio_stock/<ticker>/<portfolio_name>')
@login_required
def remove_portfolio_stock(ticker, portfolio_name):
    current_user.remove_portfolio_stock(ticker, portfolio_name)
    return redirect(url_for('user_portfolios'))


@app.route('/add_portfolio_stock/<ticker>/<amount>/<portfolio_name>')
@login_required
def add_portfolio_stock(ticker, amount, portfolio_name):
    current_user.add_portfolio_stock(ticker, amount, portfolio_name)
    return redirect(url_for('user_portfolios'))


@app.route('/delete_portfolio/<portfolio_name>')
@login_required
def delete_porfolio(portfolio_name):
    current_user.delete_portfolio(portfolio_name)
    return redirect(url_for('user_portfolios'))


@app.route('/create_portfolio.html', methods=['GET', 'POST'])
@login_required
def create_portfolio():
    if request.method == 'POST':
        portfolio_name = request.form['portfolio_name']
        if (current_user.create_portfolio(portfolio_name)):
            return redirect(url_for('user_portfolios'))
        else:
            return Response(status="401")
    return render_template('create_portfolio.html')

# @app.route('/logout.html')
# def logout():
#     login_service.logout_session_user(current_user)
#     logout_user()
#     return redirect(url_for('index'))

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


@app.route('/profile.html')
@login_required
def work():
    return render_template('profile.html')


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
