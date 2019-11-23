class watchlistMWorker():

    def create_watchlist_stock_list(self, rows):
        tickers = []
        for row in rows:
            tickers.append(row[1])
        return tickers

    def create_watchlist_json(self, rows):
        watchlist_data = {}
        for row in rows:
            row_data = {}
            row_data["ticker"] = row[1]
            row_data["time_added"] = row[2]
            watchlist_data[str(row[0])] = row_data
        return watchlist_data

    def check_watchlist_stock(self, ticker, watchlist_tickers):
        if ticker in watchlist_tickers:
            return False
        else:
            return True
