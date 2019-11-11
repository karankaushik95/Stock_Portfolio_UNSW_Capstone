import sqlite3


def bootstrap_watchlist_db():
    connection = sqlite3.connect('watchlist.db')
    c = connection.cursor()
    sql_command = """CREATE TABLE if not exists watchlist (id INTEGER PRIMARY KEY, user_id INTEGER NOT NULL,
            static_id INTEGER, status INTEGER, date DATE, time DATETIME);"""
    c.execute(sql_command)
    connection.commit()
    connection.close()


bootstrap_watchlist_db()
