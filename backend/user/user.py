from flask_login import UserMixin
import sqlite3
from time import gmtime, strftime


class User(UserMixin):

    def __init__(self, user_id):
        self.email = user_id

    def get_portfolio_names(self):
        db_name = 'db/users/' + str(self.email)
        connection = sqlite3.connect(db_name)
        cursor = connection.cursor()
        sql_command = """SELECT * FROM portfolio_names;"""
        cursor.execute(sql_command)
        rows = cursor.fetchall()
        portfolio_names = []
        for row in rows:
            portfolio_names.append(row[1])
        connection.close()
        return portfolio_names

    def remove_portfolio_stock(self, ticker, portfolio_name):
        db_name = 'db/users/' + str(self.email)
        connection = sqlite3.connect(db_name)
        cursor = connection.cursor()
        sql_command = """DELETE FROM "{}" WHERE ticker = "{}";"""
        sql_query = sql_command.format(portfolio_name, ticker)
        cursor.execute(sql_query)
        connection.commit()
        connection.close()

    def add_portfolio_stock(self, ticker, amount, portfolio_name):
        db_name = 'db/users/' + str(self.email)
        connection = sqlite3.connect(db_name)
        cursor = connection.cursor()
        sql_command = """INSERT INTO "{}" (id, ticker, amount, time_added) VALUES (NULL, "{}", "{}", "{}");"""
        sql_query = sql_command.format(portfolio_name, ticker, amount, strftime("%Y-%m-%d %H:%M:%S", gmtime()))
        cursor.execute(sql_query)
        connection.commit()
        connection.close()

    def remove_watchlist_stock(self, ticker):
        db_name = 'db/users/' + str(self.email)
        connection = sqlite3.connect(db_name)
        cursor = connection.cursor()
        sql_command = """DELETE FROM watchlist WHERE ticker = "{}";"""
        sql_query = sql_command.format(ticker)
        cursor.execute(sql_query)
        connection.commit()
        connection.close()

    def add_watchlist_stock(self, ticker):
        db_name = 'db/users/' + str(self.email)
        connection = sqlite3.connect(db_name)
        cursor = connection.cursor()
        sql_command = """INSERT INTO watchlist (id, ticker, time_added) VALUES (NULL, "{}", "{}");"""
        sql_query = sql_command.format(ticker, strftime("%Y-%m-%d %H:%M:%S", gmtime()))
        cursor.execute(sql_query)
        connection.commit()
        connection.close()

    def delete_portfolio(self, portfolio_name):
        db_name = 'db/users/' + str(self.email)
        connection = sqlite3.connect(db_name)
        cursor = connection.cursor()
        sql_command = """DELETE FROM portfolio_names WHERE name = "{}";"""
        sql_query = sql_command.format(portfolio_name)
        cursor.execute(sql_query)

        sql_command = """DROP TABLE "{}";"""
        sql_query = sql_command.format(portfolio_name)
        cursor.execute(sql_query)
        connection.commit()
        connection.close()

    def create_portfolio(self, portfolio_name):
        portfolio_names = self.get_portfolio_names()
        if portfolio_name in portfolio_names or portfolio_name == "watchlist":
            return False

        db_name = 'db/users/' + str(self.email)
        connection = sqlite3.connect(db_name)
        cursor = connection.cursor()
        sql_command = """INSERT INTO portfolio_names (name) VALUES ("{}");"""
        sql_query = sql_command.format(portfolio_name)
        cursor.execute(sql_query)

        sql_command = """CREATE TABLE if not exists "{}" (id INTEGER PRIMARY KEY, ticker VARCHAR(20), amount INTEGER,
                      time_added TEXT);"""
        sql_query = sql_command.format(portfolio_name)
        cursor.execute(sql_query)
        connection.commit()
        connection.close()
        return True

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

    def get_portfolios(self):
        db_name = 'db/users/' + str(self.email)
        connection = sqlite3.connect(db_name)
        cursor = connection.cursor()
        portfolio_names = self.get_portfolio_names()
        portfolios = {}
        for portfolio in portfolio_names:
            sql_command = """ SELECT * FROM "{}";"""
            sql_query = sql_command.format(portfolio)
            cursor.execute(sql_query)
            rows = cursor.fetchall()
            print(rows)
            portfolio_data = {}
            for row in rows:
                print(row)
                row_data = {}
                row_data["ticker"] = row[1]
                row_data["amount"] = row[2]
                row_data["time_added"] = row[3]
                portfolio_data[str(row[0])] = row_data
            portfolios[str(portfolio)] = portfolio_data
        return portfolios

    def get_watchlist(self):
        db_name = 'db/users/' + str(self.email)
        connection = sqlite3.connect(db_name)
        cursor = connection.cursor()
        sql_command = """ SELECT * FROM watchlist;"""
        cursor.execute(sql_command)
        rows = cursor.fetchall()
        watchlist_data = {}
        for row in rows:
            row_data = {}
            row_data["ticker"] = row[1]
            row_data["time_added"] = row[2]
            watchlist_data[str(row[0])] = row_data
        return watchlist_data

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return True

    def get_id(self):
        return self.email
