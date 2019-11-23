import sqlite3
import requests
from os import path
import json


def bootstrap_db():
    bootstrap_users_db()
    # populate_users_db()


def bootstrap_users_db():
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()
    sql_command = """ CREATE TABLE users (name VARCHAR(50), email VARCHAR(100), password VARCHAR(100));"""
    cursor.execute(sql_command)
    connection.commit()
    connection.close()


def populate_users_db():
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()
    sql = """ INSERT INTO users (name, email, password) VALUES ("{}", "{}", "{}");"""
    query = sql.format('jack', 'jack', 'jack')
    cursor.execute(query)
    connection.commit()
    connection.close()


if __name__ == '__main__':
    bootstrap_db()
