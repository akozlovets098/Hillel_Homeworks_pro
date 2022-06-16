from datetime import date, timedelta
import random
import sqlite3

import requests

from app import app


def get_connection(db_name: str):
    connection = sqlite3.connect(db_name)
    connection.row_factory = sqlite3.Row
    return connection


def add_activity(name, details, category, date):
    with get_connection(app.config.get('DB_URL')) as db_connect:
        cursor = db_connect.cursor()
        if cursor.execute('SELECT id FROM categories WHERE category LIKE ?', (category,)).fetchone() is None:
            cursor.execute('''
                INSERT INTO categories(category)
                VALUES(?)
            ''', (category,))
        cursor.execute('''
            INSERT INTO activities(name, details, category, date)
            VALUES (?, ?, ?, ?)
        ''', (name,
              details,
              cursor.execute('SELECT id FROM categories WHERE category LIKE ?', (category,)).fetchone()[0],
              date))
    cursor.close()
    db_connect.commit()


def init_db(db_name: str):
    with get_connection(db_name) as db_connect:
        cursor = db_connect.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS categories(
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                category VARCHAR NOT NULL UNIQUE)
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS activities(
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                name VARCHAR NOT NULL,
                details VARCHAR,
                category INTEGER,
                date DATE,
                FOREIGN KEY (category) REFERENCES categories(id))
        ''')
        cursor.close()
        db_connect.commit()

        for i in range(10):
            activity = requests.get('http://www.boredapi.com/api/activity/').json()
            add_activity(name=activity['activity'],
                       details=f"Participants needed: {activity['participants']}, price is {activity['price']}",
                       category=activity['type'],
                       date=random.choice([date.today() + timedelta(days=i) for i in range(8)]))


def list_of_categories(db_name):
    with get_connection(db_name) as db_connect:
        cursor = db_connect.cursor()
        categories = cursor.execute('SELECT category FROM categories').fetchall()
        return [category[0] for category in categories]