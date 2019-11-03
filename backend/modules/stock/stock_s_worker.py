from server import app
import json
import requests


class stockSWorker():

    @staticmethod
    def av_quote(ticker):
        url = app.config["AV_URL"] + "GLOBAL_QUOTE&symbol={}" + app.config["AV_TOKEN"]
        url = url.format(ticker)
        data = requests.get(url)
        json_data = json.loads(data.text)
        return json_data

    @staticmethod
    def av_time_series(ticker, interval, series, adjusted):
        if series == 'INTRADAY':
            url = app.config["AV_URL"] + "TIME_SERIES_INTRADAY&symbol={}&interval={}" + app.config["AV_TOKEN"]
            url = url.format(ticker, interval)
        elif adjusted:
            url = app.config["AV_URL"] + "TIME_SERIES_{}_ADJUSTED&symbol={}" + app.config["AV_TOKEN"]
            url = url.format(series, ticker)
        else:
            url = app.config["AV_URL"] + "TIME_SERIES_{}&symbol={}" + app.config["AV_TOKEN"]
            url = url.format(series, ticker)
        data = requests.get(url)
        json_data = json.loads(data.text)
        return json_data
