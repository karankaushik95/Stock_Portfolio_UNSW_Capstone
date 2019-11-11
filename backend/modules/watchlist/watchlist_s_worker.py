import sqlite3
from datetime import date
import time


class Watchlist():

    @staticmethod
    def new_stock(user_id, static_id):
        connection = sqlite3.connect('watchlist.db')
        cursor = connection.cursor()
        status = 1
        today = date.today()
        time_stamp = time.time()
        sql = f""" INSERT INTO watchlist (user_id, static_id, status, date, time) VALUES ("{user_id}", "{static_id}", "{status}", "{today}", "{time_stamp}");"""
        cursor.execute(sql)
        connection.commit()
        connection.close()

    @staticmethod
    def remove_stock(user_id, static_id):
        connection = sqlite3.connect('watchlist.db')
        cursor = connection.cursor()
        status = 0
        sql = f""" UPDATE watchlist set status = 0 where user_id = {user_id} AND static_id = {static_id};"""
        cursor.execute(sql)
        connection.commit()
        connection.close()

    @staticmethod
    def show_watchlist(user_id):
        connection = sqlite3.connect('watchlist.db')
        cursor = connection.cursor()
        sql = f'SELECT * from watchlist where user_id = {user_id} AND status = 1'
        cursor.execute(sql)
        results = cursor.fetchall()
        connection.commit()
        connection.close()

        reply = []
        for each_result in results:
            reply.append({'WATCHLIST_ID': each_result[0],
                          'USER_ID': each_result[1],
                          'STATIC_ID': each_result[2],
                          'STATUS': each_result[3],
                          'DATE': each_result[4],
                          'TIME': each_result[5]})
        return reply

# Watchlist.new_stock(1,2)
# Watchlist.new_stock(1,3)
# Watchlist.new_stock(2,2)
# Watchlist.new_stock(2,3)
# print(Watchlist.show_watchlist(1))
# print()
# print(Watchlist.show_watchlist(2))
# print()
# Watchlist.remove_stock(1,3)
# Watchlist.remove_stock(2,3)
# print(Watchlist.show_watchlist(1))
# print()
# print(Watchlist.show_watchlist(2))
