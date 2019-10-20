from flask import request, render_template, redirect, url_for
from server import app
import json
import requests
from service.login.login_data_access import LoginServices as LoginService

@app.route('/')
def test_api():
    url = app.config["API_BASE_URL"] + "/AAPL/quote" + app.config["API_TOKEN"]
    data = requests.get(url)
    json_data = json.loads(data.text)
    return json.dumps(json_data)


@app.route('/index')
def test_html():
    return render_template('index.html')

@app.route('/login', methods = ["GET", "POST"])
def login_html():
    if (request.method == "POST"):
        email = request.form["email"]
        password = request.form["password"]
        if (LoginService.check(email, password)):
            return redirect(url_for("test_html"))
        else:
            return redirect(url_for("login_html"))
    return render_template('login.html')

@app.route('/signup', methods = ["GET", "POST"])
def signup_html():
    if (request.method == "POST"):
        email = request.form["email"]
        password = request.form["password"]
        if (LoginService.user_exists(email)):
            return redirect(url_for("signup_html"))
        LoginService.new_user(email, password)
        return redirect(url_for("login_html"))
    return render_template('signup.html')

