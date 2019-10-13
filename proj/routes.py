from flask import render_template
from server import app
import json
import requests


@app.route('/')
def test_api():
    url = app.config["API_BASE_URL"] + "/AAPL/quote" + app.config["API_TOKEN"]
    data = requests.get(url)
    json_data = json.loads(data.text)
    return json.dumps(json_data)


@app.route('/index')
def test_html():
    return render_template('index.html')
