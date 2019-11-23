import sqlite3
from time import gmtime, strftime


class watchlistSWorker():

    def remove_watchlist_stock(self, email, ticker):
        db_name = 'db/users/' + str(email)
        connection = sqlite3.connect(db_name)
        cursor = connection.cursor()
        sql_command = """DELETE FROM watchlist WHERE ticker = "{}";"""
        sql_query = sql_command.format(ticker)
        cursor.execute(sql_query)
        connection.commit()
        connection.close()

    def add_watchlist_stock(self, email, ticker):
        db_name = 'db/users/' + str(email)
        connection = sqlite3.connect(db_name)
        cursor = connection.cursor()
        sql_command = """INSERT INTO watchlist (id, ticker, time_added) VALUES (NULL, "{}", "{}");"""
        sql_query = sql_command.format(ticker, strftime("%Y-%m-%d %H:%M:%S", gmtime()))
        cursor.execute(sql_query)
        connection.commit()
        connection.close()

    def get_watchlist(self, email):
        db_name = 'db/users/' + str(email)
        connection = sqlite3.connect(db_name)
        cursor = connection.cursor()
        sql_command = """ SELECT * FROM watchlist;"""
        cursor.execute(sql_command)
        rows = cursor.fetchall()
        return rows
