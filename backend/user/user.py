from flask_login import UserMixin
import sqlite3
from modules.portfolio.portfolio_s_worker import portfolioSWorker
from modules.portfolio.portfolio_m_worker import portfolioMWorker
from modules.watchlist.watchlist_s_worker import watchlistSWorker
from modules.watchlist.watchlist_m_worker import watchlistMWorker


class User(UserMixin):

    def __init__(self, user_id):
        self.email = user_id
        self.ps_worker = portfolioSWorker()
        self.pm_worker = portfolioMWorker()
        self.ws_worker = watchlistSWorker()
        self.wm_worker = watchlistMWorker()

    def remove_watchlist_stock(self, ticker):
        self.ws_worker.remove_watchlist_stock(self.email, ticker)

    def add_watchlist_stock(self, ticker):
        sql_data = self.ws_worker.get_watchlist(self.email)
        watchlist_data = self.wm_worker.create_watchlist_stock_list(sql_data)
        stock_flag = self.wm_worker.check_watchlist_stock(ticker, watchlist_data)
        if stock_flag:
            self.ws_worker.add_watchlist_stock(self.email, ticker)
            return True
        else:
            return False

    def get_watchlist(self):
        sql_data = self.ws_worker.get_watchlist(self.email)
        watchlist_data = self.wm_worker.create_watchlist_json(sql_data)
        return watchlist_data

    def get_portfolio_names(self):
        sql_data = self.ps_worker.get_portfolio_names(self.email)
        portfolio_data = self.pm_worker.create_portfolios_list(sql_data)
        return portfolio_data

    def remove_portfolio_stock(self, ticker, portfolio_name):
        self.ps_worker.remove_portfolio_stock(self.email, ticker, portfolio_name)

    def add_portfolio_stock(self, ticker, amount, portfolio_name):
        sql_data = self.ps_worker.get_portfolio(self.email, portfolio_name)
        portfolio_data = self.pm_worker.create_portfolio_stock_list(sql_data)
        stock_flag = self.pm_worker.check_portfolio_stock(ticker, portfolio_data)
        if stock_flag:
            self.ps_worker.add_portfolio_stock(self.email, ticker, amount, portfolio_name)
            return True
        else:
            self.ps_worker.update_portfolio_stock(self.email, ticker, amount, portfolio_name)
            return False

    def delete_portfolio(self, portfolio_name):
        self.ps_worker.delete_portfolio(self.email, portfolio_name)

    def create_portfolio(self, portfolio_name):
        sql_data = self.ps_worker.get_portfolio_names(self.email)
        portfolio_data = self.pm_worker.create_portfolios_list(sql_data)
        name_flag = self.pm_worker.check_portfolio_names(portfolio_name, portfolio_data)
        if name_flag:
            self.ps_worker.create_portfolio(self.email, portfolio_name)
            return True
        else:
            return False

    def get_portfolios(self):
        sql_data = self.ps_worker.get_portfolio_names(self.email)
        portfolio_data = self.pm_worker.create_portfolios_list(sql_data)
        portfolios = self.pm_worker.create_portfolio_json(self.email, portfolio_data)
        return portfolios

    def get_details(self):
        connection = sqlite3.connect('db/users.db')
        cursor = connection.cursor()
        sql_command = """ SELECT * FROM users WHERE email="{}";"""
        sql_query = sql_command.format(str(self.email))
        cursor.execute(sql_query)
        rows = cursor.fetchall()
        user_data = {}
        user_data["name"] = rows[0][0]
        user_data["email"] = rows[0][1]
        return user_data
    
    def update_password(self, new_pass):
        connection = sqlite3.connect('db/users.db')
        cursor = connection.cursor()
        sql_command = """ UPDATE users SET password = "{}" WHERE email = "{}";"""
        sql_query = sql_command.format(str(new_pass), str(self.email))
        cursor.execute(sql_query)
        connection.close()

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return True

    def get_id(self):
        return self.email
