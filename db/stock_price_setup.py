import sqlite3
import requests
import json


def bootstrap_db():
    bootstrap_stock_price_db()
    populate_stock_price_db()


def bootstrap_stock_price_db():
    connection = sqlite3.connect('stock_price.db')
    cursor = connection.cursor()
    sql_command = """ CREATE TABLE price (id INTEGER PRIMARY KEY, ticker VARCHAR(30), price FLOAT(10,2));"""
    cursor.execute(sql_command)
    connection.commit()
    connection.close()


def populate_stock_price_db():
    connection = sqlite3.connect('stock_price.db')
    cursor = connection.cursor()

    sql = """ INSERT INTO price (id, ticker, price) VALUES (NULL, "{}", "{}");"""
    query = sql.format('AAPL', str(265.76))
    cursor.execute(query)

    sql = """ INSERT INTO price (id, ticker, price) VALUES (NULL, "{}", "{}");"""
    query = sql.format('MSFT', str(149.97))
    cursor.execute(query)

    sql = """ INSERT INTO price (id, ticker, price) VALUES (NULL, "{}", "{}");"""
    query = sql.format('AMZN', str(1739.49))
    cursor.execute(query)

    sql = """ INSERT INTO price (id, ticker, price) VALUES (NULL, "{}", "{}");"""
    query = sql.format('GOOGL', str(1333.54))
    cursor.execute(query)

    connection.commit()
    connection.close()


if __name__ == '__main__':
    bootstrap_db()
