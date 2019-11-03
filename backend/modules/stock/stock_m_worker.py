from decimal import Decimal
from modules.stock.stock_s_worker import stockSWorker
import json
import datetime


class stockMWorker():

    @staticmethod
    def remove_keys_iex(json_data):
        del json_data['calculationPrice']
        del json_data['latestSource']
        del json_data['latestUpdate']
        del json_data['delayedPrice']
        del json_data['delayedPriceTime']
        del json_data['extendedPrice']
        del json_data['extendedChange']
        del json_data['extendedChangePercent']
        del json_data['extendedPriceTime']
        del json_data['iexMarketPercent']
        del json_data['iexVolume']
        del json_data['avgTotalVolume']
        del json_data['iexBidPrice']
        del json_data['iexBidSize']
        del json_data['iexAskPrice']
        del json_data['iexAskSize']
        del json_data['lastTradeTime']
        del json_data['isUSMarketOpen']

    @staticmethod
    def av_tidy_quote(json_data):
        quote_data = json_data["Global Quote"]
        del quote_data["07. latest trading day"]
        json_data["Global Quote"] = quote_data

    @staticmethod
    def av_create_json(quote_data, time_series):
        json_data = quote_data
        json_data["Time Series"] = time_series
        return json_data

    @staticmethod
    def av_market_cap(json_data):
        quote_data = json_data["Global Quote"]
        price = Decimal(quote_data["05. price"])
        volume = int(quote_data["06. volume"])
        market_cap = price * volume
        quote_data["market cap"] = str(market_cap)
        json_data["Global Quote"] = quote_data

    @staticmethod
    def av_daily_range(json_data, ticker):
        day_series = stockSWorker.av_time_series(ticker, '5min', 'INTRADAY', True)
        time_series = day_series["Time Series (5min)"]
        today = datetime.date.today()
        counter = 0
        max_price = -1.0
        min_price = float("inf")
        for step in time_series:
            date_time = step.split(" ")
            if counter == 0:
                today = date_time[0]
            if date_time[0] != today:
                break

            high = float(time_series[step]["2. high"])
            if high > max_price:
                max_price = high

            low = float(time_series[step]["3. low"])
            if low < min_price:
                min_price = low

            counter += 1

        quote_data = json_data["Global Quote"]
        quote_data["daily low"] = str(min_price)
        quote_data["daily high"] = str(max_price)
        json_data["Global Quote"] = quote_data

    @staticmethod
    def av_52_high_low(json_data, ticker):
        day_series = shareSWorker.av_time_series(ticker, '0', 'WEEKLY', True)
        time_series = day_series["Weekly Adjusted Time Series"]
        counter = 0
        max_price = -1.0
        min_price = float("inf")
        for step in time_series:
            if counter >= 52:
                break
            high = float(time_series[step]["2. high"])
            if high > max_price:
                max_price = high

            low = float(time_series[step]["3. low"])
            if low < min_price:
                min_price = low

            counter += 1

        quote_data = json_data["Global Quote"]
        quote_data["52 low"] = str(min_price)
        quote_data["52 high"] = str(max_price)
        json_data["Global Quote"] = quote_data
