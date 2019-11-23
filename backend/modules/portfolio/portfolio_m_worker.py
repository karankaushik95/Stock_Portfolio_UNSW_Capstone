from modules.portfolio.portfolio_s_worker import portfolioSWorker


class portfolioMWorker():

    def create_portfolios_list(self, rows):
        portfolio_names = []
        for row in rows:
            portfolio_names.append(row[1])
        return portfolio_names

    def create_portfolio_stock_list(self, rows):
        tickers = []
        for row in rows:
            tickers.append(row[1])
        return tickers

    def check_portfolio_names(self, portfolio_name, portfolio_names):
        if portfolio_name in portfolio_names or portfolio_name == "watchlist":
            return False
        else:
            return True

    def check_portfolio_stock(self, ticker, portfolio_tickers):
        if ticker in portfolio_tickers:
            return False
        else:
            return True

    def create_portfolio_json(self, email, portfolio_names):
        ps_worker = portfolioSWorker()
        portfolios = {}
        for portfolio in portfolio_names:
            rows = ps_worker.get_portfolio(email, portfolio)
            portfolio_data = {}
            for row in rows:
                print(row)
                row_data = {}
                row_data["ticker"] = row[1]
                row_data["price"] = str(0)
                row_data["amount"] = row[2]
                row_data["time_added"] = row[3]
                portfolio_data[str(row[0])] = row_data
            portfolios[str(portfolio)] = portfolio_data
