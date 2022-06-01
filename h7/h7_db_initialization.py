import sqlite3


with sqlite3.connect('purchase_list.sqlite') as db_connection:
    cursor = db_connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS purchases(
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            name TEXT NOT NULL,
            category TEXT,
            quantity INTEGER,
            price REAL,
            user TEXT)
        ''')

    cursor.execute('''
        INSERT INTO 
            purchases(name, category, quantity, price, user)
        VALUES 
            ('Snickers', 'Sweets', 2, 24.5, 'Austin'),
            ('Pepsi', 'Drinks', 1, 20, 'Rodgers'),
            ('Sour cream', 'Sauces', 1, 19.7, 'Austin'),
            ('Ketchup', 'Sauces', 3, 15.13, 'Jakobs'),
            ('French fries', 'Snacks', 1, 30, 'Austin'),
            ('M&Ms', 'Sweets', 2, 13.9, 'Rodgers'),
            ('Coffee', 'Drinks', 1, 18.6, 'Jakobs')
        ''')

    cursor.close()
    db_connection.commit()