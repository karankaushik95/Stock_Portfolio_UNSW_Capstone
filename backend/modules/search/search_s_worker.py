from server import app
import json
import requests


class searchSWorker():

    @staticmethod
    def av_search_string(string):
        url = app.config["AV_URL"] + "SYMBOL_SEARCH&keywords={}" + app.config["AV_TOKEN"]
        url = url.format(string)
        data = requests.get(url)
        json_data = json.loads(data.text)
        return json_data
