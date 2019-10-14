# We will use this for bootstrapping
import sqlite3
import os.path
from os import path
from server import app


def bootstrap():
    if not path.exists('db/stock.db'):
        bootstrap_db()

    bootstrap_system()


def bootstrap_db():
    connection = sqlite3.connect("db/stock.db")
    cursor = connection.cursor()

    sql_command = """ CREATE TABLE static (ticker VARCHAR(5) PRIMARY KEY, exchange VARCHAR(30), name VARCHAR(100),
                  type VARCHAR(2), region VARCHAR(30), currency VARCHAR(6), description VARCHAR(1000),
                  industry VARCHAR(100), sector VACHAR(100), website VARCHAR(100), ceo VARCHAR(100),
                  employees INTEGER);"""

    cursor.execute(sql_command)

    sql_command = """CREATE TABLE volatile (ticker VARCHAR(5) PRIMARY KEY);"""

    cursor.execute(sql_command)
    connection.commit()
    connection.close()

    populate_stock_db()


def bootstrap_system():
    # USED FOR LATER ON
    update_stock_db()


def populate_stock_db():
    connection = sqlite3.connect("db/stock.db")
    cursor = connection.cursor()
    sql_command = """INSERT INTO static (ticker, exchange, name, type, region, currency, description, industry, sector,
                  website, ceo, employees) VALUES ("AAPL", "NASDAQ", "Apple Inc.", "cs", "USA", "USD", "GOOD STOCK",
                  "Telecommunications", "Private", "apple.com", "Tim Cook", "67");"""
    cursor.execute(sql_command)
    connection.commit()
    connection.close()


def update_stock_db():
    connection = sqlite3.connect("db/stock.db")
    cursor = connection.cursor()
    sql_command = """UPDATE static SET exchange='NASDAK' WHERE ticker='AAPL';"""
    cursor.execute(sql_command)
    sql_command = """SELECT * FROM static WHERE ticker='AAPL';"""
    cursor.execute(sql_command)
    r = cursor.fetchall()
    print(r)
    connection.commit()
    connection.close()
