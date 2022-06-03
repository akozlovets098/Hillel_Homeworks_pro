import random
import sqlite3

professions = ['teacher', 'plumber', 'engineer', 'doctor', 'pilot', 'accountant', 'trainer', 'cleaner', 'veterinarian',
               'architect']
genders = ['male', 'female']

with sqlite3.connect('people.sqlite') as db_connection:
    db_connection.row_factory = sqlite3.Row
    cursor = db_connection.cursor()

    cursor.execute('''
        DROP TABLE IF EXISTS professions
    ''')
    cursor.execute('''
        DROP TABLE IF EXISTS genders
    ''')
    cursor.execute('''
        DROP TABLE IF EXISTS people
    ''')

    cursor.execute('''
        PRAGMA foreign_keys = ON
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS professions(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            profession VARCHAR NOT NULL)
    ''')
    cursor.executemany('''
        INSERT INTO professions(profession)
            VALUES (:profession)
    ''', [{'profession': profession} for profession in professions])

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS genders(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            gender VARCHAR NOT NULL)
    ''')
    cursor.executemany('''
        INSERT INTO genders(gender)
            VALUES (:gender)
    ''', [{'gender': gender} for gender in genders])

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS people(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name VARCHAR NOT NULL,
            last_name VARCHAR NOT NULL,
            gender INTEGER NOT NULL,
            salary INTEGER,
            profession INTEGER,
            email VARCHAR,
            age INTEGER NOT NULL,
            FOREIGN KEY(gender) REFERENCES genders(id),
            FOREIGN KEY(profession) REFERENCES professions(id))
    ''')
    cursor.execute(f'''
        INSERT INTO people(first_name, last_name, gender, salary, profession, email, age)
        VALUES
            ('Mary', 'Smith', 2, {random.randint(500, 10000)}, {random.randint(1, 10)}, NULL, {random.randint(20, 75)}),
            ('John', 'Miles', 1, {random.randint(500, 10000)}, NULL, 'jmiles@gmail.com', {random.randint(20, 75)}),
            ('Jack', 'Andrews', 1, {random.randint(500, 10000)}, {random.randint(1, 10)}, NULL, {random.randint(20, 75)}),
            ('Ann', 'Johnson', 2, {random.randint(500, 10000)}, NULL, 'annjohns@yahoo.com', {random.randint(20, 75)}),
            ('Rose', 'Miller', 2, {random.randint(500, 10000)}, {random.randint(1, 10)}, 'rmiller@sky.net', {random.randint(20, 75)}),
            ('Andrew', 'Jones', 1, {random.randint(500, 10000)}, NULL, NULL, {random.randint(20, 75)}),
            ('Juliet', 'Williams', 2, {random.randint(500, 10000)}, {random.randint(1, 10)}, NULL, {random.randint(20, 75)}),
            ('Randy', 'Anderson', 1, {random.randint(500, 10000)}, {random.randint(1, 10)}, NULL, {random.randint(20, 75)}),
            ('Liam', 'Garcia', 1, {random.randint(500, 10000)}, NULL, NULL, {random.randint(20, 75)}),
            ('Mary', 'Davis', 2, {random.randint(500, 10000)}, {random.randint(1, 10)}, NULL, {random.randint(20, 75)}),
            ('Jack', 'Lopez', 1, {random.randint(500, 10000)}, {random.randint(1, 10)}, NULL, {random.randint(20, 75)}),
            ('Stasy', 'Willson', 2, {random.randint(500, 10000)}, NULL, 'st.willson@gmail.com', {random.randint(20, 75)}),
            ('James', 'Moore', 1, {random.randint(500, 10000)}, {random.randint(1, 10)}, NULL, {random.randint(20, 75)}),
            ('Deryl', 'Lee', 1, {random.randint(500, 10000)}, {random.randint(1, 10)}, NULL, {random.randint(20, 75)}),
            ('Mike', 'Thompson', 1, {random.randint(500, 10000)}, NULL, 'm.thompson@outlook.com', {random.randint(20, 75)}),
            ('Veronika', 'White', 2, {random.randint(500, 10000)}, NULL, NULL, {random.randint(20, 75)}),
            ('Edith', 'Clark', 2, {random.randint(500, 10000)}, {random.randint(1, 10)}, NULL, {random.randint(20, 75)}),
            ('Josh', 'Lewis', 1, {random.randint(500, 10000)}, NULL, NULL, {random.randint(20, 75)}),
            ('Donald', 'Robinson', 1, {random.randint(500, 10000)}, NULL, 'drobinson75@gmail.com', {random.randint(20, 75)}),
            ('Bob', 'Allen', 1, {random.randint(500, 10000)}, {random.randint(1, 10)}, NULL, {random.randint(20, 75)})
    ''')

    cursor.execute('''
        INSERT INTO people(first_name, last_name, gender, age)
        VALUES
            ('Laurence', 'Wachowski', 1, 40),
            ('Andrew', 'Wachowski', 1, 34)
    ''')

    cursor.execute('''
        UPDATE people
        SET gender = 2
        WHERE last_name = 'Wachowski'
    ''')
    cursor.execute('''
        UPDATE people
        SET first_name = 'Lana'
        WHERE first_name = 'Laurence' AND last_name = 'Wachowski'
    ''')
    cursor.execute('''
        UPDATE people
        SET first_name = 'Lilly'
        WHERE first_name = 'Andrew' AND last_name = 'Wachowski'
    ''')

    cursor.execute('''
        INSERT INTO genders(gender)
        VALUES ('non-binary')
    ''')

    cursor.execute('''
        UPDATE people
        SET gender = 3
        WHERE first_name IN ('Mary', 'Jack', 'Mike', 'Veronika')
    ''')

    nonbinary_list = cursor.execute('''
        SELECT p.first_name, p.last_name, g.gender, p.salary, p.profession, p.email, p.age
        FROM people AS p
        JOIN genders AS g ON p.gender = g.id
        WHERE p.gender = 3
    ''')
    for item in nonbinary_list:
        print(dict(item))

    cursor.execute('''
        UPDATE people
        SET email = first_name ||'.' || last_name || '@sky.net'
        WHERE email IS NULL 
    ''')

    cursor.close()
    db_connection.commit()


