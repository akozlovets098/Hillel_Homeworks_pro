import sqlite3
from flask import Flask, render_template

app = Flask('Purchases')


def get_all_purchases():
    with sqlite3.connect('purchase_list.sqlite') as db_connection:
        db_connection.row_factory = sqlite3.Row
        cursor = db_connection.cursor()
        purchases_cursor = cursor.execute("""
            SELECT * FROM purchases
        """)
        return purchases_cursor


def get_purchases_by_category(category):
    with sqlite3.connect('purchase_list.sqlite') as db_connection:
        db_connection.row_factory = sqlite3.Row
        cursor = db_connection.cursor()
        purchases_cursor = cursor.execute(f"""
            SELECT * FROM purchases
            WHERE category LIKE '{category}'
        """)
        return purchases_cursor


def get_purchases_by_user(user):
    with sqlite3.connect('purchase_list.sqlite') as db_connection:
        db_connection.row_factory = sqlite3.Row
        cursor = db_connection.cursor()
        purchases_cursor = cursor.execute(f"""
            SELECT * FROM purchases
            WHERE user LIKE '{user}'
        """)
        return purchases_cursor


def create_purchases_dict(purchases_cursor):
    purchases = []
    for item in purchases_cursor:
        purchases.append(dict(item))
    return purchases


@app.route('/')
def hello():
    return render_template('main_page.html')


@app.route('/all')
def all_purchases():
    purchases = create_purchases_dict(get_all_purchases())
    return render_template('purchases_list.html', category='all categories and users', purchases=purchases)


@app.route('/category/<category>')
def purchases_by_category(category):
    purchases = create_purchases_dict(get_purchases_by_category(category))
    if len(purchases) > 0:
        return render_template('purchases_list.html', category=f'{category} category', purchases=purchases)
    return 'Sorry, no such category'


@app.route('/user/<user>')
def purchases_by_user(user):
    purchases = create_purchases_dict(get_purchases_by_user(user))
    if len(purchases) > 0:
        return render_template('purchases_list.html', category=f'user {user}', purchases=purchases)
    return 'Sorry, no such user'


if __name__ == '__main__':
    app.run()