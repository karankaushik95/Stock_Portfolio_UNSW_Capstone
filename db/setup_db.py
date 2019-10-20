import sqlite3
import requests
from os import path
import json
import csv


def bootstrap():
    if not path.exists('tickers.db'):
        bootstrap_tickers_db()
        populate_tickers_db()

    if not path.exists('stock.db'):
        bootstrap_stock_db()
        populate_stock_db()
        
    if not path.exists('users.db'):
        bootstrap_users_db()
        populate_users_db()

def bootstrap_users_db():
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()
    sql_command = """ CREATE TABLE users(email, password);"""
    cursor.execute(sql_command)
    connection.commit()
    connection.close()
    
def populate_users_db():
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()
    with open('users.csv', mode = 'r') as users:
            reader = csv.reader(users)
            for row in reader:
                sql = """ INSERT INTO users (email, password) VALUES ("{}", "{}");"""
                query = sql.format(row[0], row[1])
                cursor.execute(query)
    connection.commit()
    connection.close()

def bootstrap_tickers_db():
    connection = sqlite3.connect('tickers.db')
    cursor = connection.cursor()
    sql_command = """ CREATE TABLE tickers(id INTEGER PRIMARY KEY, ticker VARCHAR(5), exchange VARCHAR(10),
                  name VARCHAR(100));"""
    cursor.execute(sql_command)
    connection.commit()
    connection.close()


def populate_tickers_db():
    connection = sqlite3.connect('tickers.db')
    cursor = connection.cursor()
    url = "https://cloud.iexapis.com/stable/ref-data/symbols?token=pk_6258cdb0c7c24d8ba34b1a1c2929e40d"
    data = requests.get(url)
    json_data = json.loads(data.text)
    i = 0
    for symbol in json_data:
        print(symbol)
        sql = """ INSERT INTO tickers (id, ticker, exchange, name) VALUES ("{}", "{}", "{}", "{}");"""
        query = sql.format(i, symbol['symbol'], symbol['exchange'], symbol['name'])
        cursor.execute(query)
        i += 1

    connection.commit()
    connection.close()


def bootstrap_stock_db():
    connection = sqlite3.connect('stock.db')
    cursor = connection.cursor()
    sql_command = """ CREATE TABLE static (id INTEGER PRIMARY KEY, ticker VARCHAR(5), exchange VARCHAR(30), name VARCHAR(100),
                  type VARCHAR(3), region VARCHAR(30), description VARCHAR(1000), industry VARCHAR(100),
                  sector VACHAR(100), website VARCHAR(100), ceo VARCHAR(100), employees INTEGER);"""

    cursor.execute(sql_command)
    sql_command = """ CREATE TABLE volatile (id INTEGER PRIMARY KEY, ticker VARCHAR(5), open FLOAT(8,2), close FLOAT(8,2),
                  high FLOAT(8,2), low FLOAT(8,2), latest FLOAT(8,2), latest_source VARCHAR(100), change FLOAT(8,2),
                  change_percent FLOAT(8,2), market_cap INTEGER, high_y FLOAT(8,2), low_y FLOAT(8,2),
                  ytd_change FLOAT(8,2));"""

    cursor.execute(sql_command)
    connection.commit()
    connection.close()


def populate_stock_db():
    connection = sqlite3.connect('stock.db')
    cursor = connection.cursor()
    url = "https://cloud.iexapis.com/stable/ref-data/symbols?token=pk_6258cdb0c7c24d8ba34b1a1c2929e40d"
    data = requests.get(url)
    json_data = json.loads(data.text)
    i = 0
    for symbol in json_data:
        url = "https://cloud.iexapis.com/stable/stock/{}/company?token=pk_6258cdb0c7c24d8ba34b1a1c2929e40d"
        url_n = url.format(symbol['symbol'])
        quote = requests.get(url_n)
        json_quote = json.loads(quote.text)
        print(json_quote)
        sql_command = """ INSERT INTO static (id, ticker, exchange, name, type, region, description, industry,
                      sector, website, ceo, employees) VALUES ("{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}",
                      "{}", "{}", "{}", "{}");"""
        sql_query = sql_command.format(i, json_quote['symbol'], json_quote['exchange'], json_quote['companyName'],
                                       json_quote['issueType'], json_quote['country'], 'blank',
                                       json_quote['industry'], json_quote['sector'], json_quote['website'],
                                       json_quote['CEO'], json_quote['employees'])

        print(sql_query)
        cursor.execute(sql_query)
        i += 1

    connection.commit()
    connection.close()
    print("Finished")


if __name__ == "__main__":
    bootstrap()
