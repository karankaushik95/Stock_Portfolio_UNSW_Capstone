import sqlite3
from time import gmtime, strftime


class portfolioSWorker():

    def get_portfolio_names(self, email):
        db_name = 'db/users/' + str(email)
        connection = sqlite3.connect(db_name)
        cursor = connection.cursor()
        sql_command = """SELECT * FROM portfolio_names;"""
        cursor.execute(sql_command)
        rows = cursor.fetchall()
        connection.close()
        return rows

    def remove_portfolio_stock(self, email, ticker, portfolio_name):
        db_name = 'db/users/' + str(email)
        connection = sqlite3.connect(db_name)
        cursor = connection.cursor()
        sql_command = """DELETE FROM "{}" WHERE ticker = "{}";"""
        sql_query = sql_command.format(portfolio_name, ticker)
        cursor.execute(sql_query)
        connection.commit()
        connection.close()

    def add_portfolio_stock(self, email, ticker, amount, portfolio_name):
        db_name = 'db/users/' + str(email)
        connection = sqlite3.connect(db_name)
        cursor = connection.cursor()
        sql_command = """INSERT INTO "{}" (id, ticker, amount, time_added) VALUES (NULL, "{}", "{}", "{}");"""
        sql_query = sql_command.format(portfolio_name, ticker, amount, strftime("%Y-%m-%d %H:%M:%S", gmtime()))
        cursor.execute(sql_query)
        connection.commit()
        connection.close()

    def update_portfolio_stock(self, email, ticker, amount, portfolio_name):
        db_name = 'db/users/' + str(email)
        connection = sqlite3.connect(db_name)
        cursor = connection.cursor()
        sql_command = """SELECT amount FROM "{}" WHERE ticker = "{}";"""
        sql_query = sql_command.format(portfolio_name, ticker)
        cursor.execute(sql_query)
        amount_raw = cursor.fetchall()
        amount_prev = int(amount_raw[0][0])
        sql_command = """UPDATE "{}" SET amount = "{}" WHERE ticker = "{}";"""
        sql_query = sql_command.format(portfolio_name, int(amount) + amount_prev, ticker)
        cursor.execute(sql_query)
        connection.commit()
        connection.close()

    def delete_portfolio(self, email, portfolio_name):
        db_name = 'db/users/' + str(email)
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

    def create_portfolio(self, email, portfolio_name):
        db_name = 'db/users/' + str(email)
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

    def get_portfolio(self, email, portfolio_name):
        db_name = 'db/users/' + str(email)
        connection = sqlite3.connect(db_name)
        cursor = connection.cursor()
        sql_command = """ SELECT * FROM "{}";"""
        sql_query = sql_command.format(portfolio_name)
        cursor.execute(sql_query)
        rows = cursor.fetchall()
        return rows
