from flask import Flask, request, render_template
import json, requests

app = Flask(__name__, template_folder='../templates')
app.config.from_envvar('PROJ_CONFIG')

@app.route('/')
def test():
    url = app.config["API_BASE_URL"] + "/AAPL/quote" + app.config["API_TOKEN"]
    data = requests.get(url)
    json_data = json.loads(data.text)
    return json.dumps(json_data)

@app.route('/index')
def test_structure():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
