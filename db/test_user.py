import sqlite3
from datetime import datetime


def test_portfolio_names():
    db_name = 'users/k@k.com'
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    sql_command = """INSERT INTO portfolio_names VALUES ("{}", "{}");"""
    sql_query = sql_command.format(0, 'portfolio1')
    cursor.execute(sql_query)
    sql_command = """INSERT INTO portfolio_names VALUES ("{}", "{}");"""
    sql_query = sql_command.format(1, 'portfolio2')
    cursor.execute(sql_query)
    connection.commit()
    connection.close()


def test_watchlist_names():
    db_name = 'users/k@k.com'
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    sql_command = """INSERT INTO watchlist_names VALUES ("{}", "{}");"""
    sql_query = sql_command.format(0, 'watchlist1')
    cursor.execute(sql_query)
    sql_command = """INSERT INTO watchlist_names VALUES ("{}", "{}");"""
    sql_query = sql_command.format(1, 'watchlist2')
    cursor.execute(sql_query)
    connection.commit()
    connection.close()


def test_portfolio():
    db_name = 'users/k@k.com'
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    table_name = "portfolio1"
    sql_command = """CREATE TABLE if not exists "{}" (id INTEGER PRIMARY KEY, ticker VARCHAR(20), amount INTEGER, time_added TEXT);"""
    sql_query = sql_command.format(table_name)
    cursor.execute(sql_query)

    table_name = "portfolio2"
    sql_command = """CREATE TABLE if not exists "{}" (id INTEGER PRIMARY KEY, ticker VARCHAR(20), amount INTEGER, time_added TEXT);"""
    sql_query = sql_command.format(table_name)
    cursor.execute(sql_query)

    sql_command = """INSERT INTO portfolio1 VALUES ("{}", "{}", "{}", "{}");"""
    sql_query = sql_command.format(0, 'AAPL', 30, str(datetime.now()))
    cursor.execute(sql_query)
    sql_command = """INSERT INTO portfolio1 VALUES ("{}", "{}", "{}", "{}");"""
    sql_query = sql_command.format(1, 'AAPL', 40, str(datetime.now()))
    cursor.execute(sql_query)
    sql_command = """INSERT INTO portfolio1 VALUES ("{}", "{}", "{}", "{}");"""
    sql_query = sql_command.format(2, 'AAPL', 50, str(datetime.now()))
    cursor.execute(sql_query)

    sql_command = """INSERT INTO portfolio2 VALUES ("{}", "{}", "{}", "{}");"""
    sql_query = sql_command.format(0, 'ANZ', 30, str(datetime.now()))
    cursor.execute(sql_query)
    sql_command = """INSERT INTO portfolio2 VALUES ("{}", "{}", "{}", "{}");"""
    sql_query = sql_command.format(1, 'ANZ', 40, str(datetime.now()))
    cursor.execute(sql_query)
    sql_command = """INSERT INTO portfolio2 VALUES ("{}", "{}", "{}", "{}");"""
    sql_query = sql_command.format(2, 'ANZ', 50, str(datetime.now()))
    cursor.execute(sql_query)

    connection.commit()
    connection.close()


def test_watchlist():
    db_name = 'users/k@k.com'
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    table_name = "watchlist1"
    sql_command = """CREATE TABLE if not exists "{}" (id INTEGER PRIMARY KEY, ticker VARCHAR(20), time_added TEXT);"""
    sql_query = sql_command.format(table_name)
    cursor.execute(sql_query)

    table_name = "watchlist2"
    sql_command = """CREATE TABLE if not exists "{}" (id INTEGER PRIMARY KEY, ticker VARCHAR(20), time_added TEXT);"""
    sql_query = sql_command.format(table_name)
    cursor.execute(sql_query)

    sql_command = """INSERT INTO watchlist1 VALUES ("{}", "{}", "{}");"""
    sql_query = sql_command.format(0, 'AAPL', str(datetime.now()))
    cursor.execute(sql_query)
    sql_command = """INSERT INTO watchlist1 VALUES ("{}", "{}", "{}");"""
    sql_query = sql_command.format(1, 'AAPL', str(datetime.now()))
    cursor.execute(sql_query)
    sql_command = """INSERT INTO watchlist1 VALUES ("{}", "{}", "{}");"""
    sql_query = sql_command.format(2, 'AAPL', str(datetime.now()))
    cursor.execute(sql_query)

    sql_command = """INSERT INTO watchlist2 VALUES ("{}", "{}", "{}");"""
    sql_query = sql_command.format(0, 'ANZ', str(datetime.now()))
    cursor.execute(sql_query)
    sql_command = """INSERT INTO watchlist2 VALUES ("{}", "{}", "{}");"""
    sql_query = sql_command.format(1, 'ANZ', str(datetime.now()))
    cursor.execute(sql_query)
    sql_command = """INSERT INTO watchlist2 VALUES ("{}", "{}", "{}");"""
    sql_query = sql_command.format(2, 'ANZ', str(datetime.now()))
    cursor.execute(sql_query)

    connection.commit()
    connection.close()


if __name__ == '__main__':
    test_portfolio_names()
    test_watchlist_names()
    test_watchlist()
    test_portfolio()
