import sqlite3
import requests
import os
import json


def bootstrap_db():
    bootstrap_users_db()
    mk_user_dir()
    # populate_users_db()


def bootstrap_users_db():
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()
    sql_command = """ CREATE TABLE users (name VARCHAR(50), email VARCHAR(100), password VARCHAR(100));"""
    cursor.execute(sql_command)
    connection.commit()
    connection.close()


def mk_user_dir():
    if os.path.exists('users/'):
        return
    else:
        os.mkdir('./users/')


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
