import requests
from flask import render_template, request, redirect
from app import app
from db import get_connection, add_activity, list_of_categories
from forms import NewActivityForm, NewCategoryForm
from random import choice
from datetime import date, timedelta


def activities_dict(activities_cursor):
    activities = []
    for activity in activities_cursor:
        activities.append(dict(activity))
    return activities


@app.route('/')
def main_page():
    return render_template('main_page.html')


@app.route('/all')
def all_activities():
    with get_connection(app.config.get('DB_URL')) as db_connection:
        cursor = db_connection.cursor()
        activities_cursor = cursor.execute('''
            SELECT a.name, a.details, c.category, a.date FROM activities a
            JOIN categories c ON c.id = a.category
        ''')
        activities = activities_dict(activities_cursor)
        return render_template('activities_list.html', category='all categories', activities=activities)


@app.route('/today')
def activity_for_today():
    with get_connection(app.config.get('DB_URL')) as db_connection:
        cursor = db_connection.cursor()
        activities_cursor = cursor.execute('''
            SELECT a.name, a.details, c.category, a.date FROM activities a
            JOIN categories c ON c.id = a.category
            WHERE a.date LIKE ?
        ''', (date.today(),))
        activities = activities_dict(activities_cursor)
        return render_template('activities_list.html', category='today\'s date', activities=activities)


@app.route('/new/activity', methods=['GET', 'POST'])
def add_new_activity():
    method = request.method
    form = NewActivityForm()
    if method == 'POST':
        if form.validate():
            add_activity(form.name.data, form.details.data, form.category.data, form.date.data)
            with get_connection(app.config.get('DB_URL')) as db_connection:
                cursor = db_connection.cursor()
                activity_name = form.name.data
                activity_data = cursor.execute('''
                    SELECT a.name, a.details, c.category, a.date FROM activities a
                    JOIN categories c ON c.id = a.category
                    WHERE a.name = ?
                ''', (activity_name,))
                activity = dict(activity_data.fetchone())
                return render_template('new_activity_added.html', activity=activity)
        else:
            return redirect(f'/new/activity')
    else:
        random_activity = requests.get('http://www.boredapi.com/api/activity/').json()
        example_activity = {
            'name': random_activity['activity'],
            'details': f"Participants needed: {random_activity['participants']}, price is {random_activity['price']}",
            'category': random_activity['type'],
            'date': choice([date.today() + timedelta(days=i) for i in range(8)])
        }
        return render_template('new_activity.html', form=form, activity=example_activity)


@app.route('/new/category', methods=['GET', 'POST'])
def add_new_category():
    method = request.method
    form = NewCategoryForm()
    if method == 'POST':
        if form.validate():
            with get_connection(app.config.get('DB_URL')) as db_connection:
                cursor = db_connection.cursor()
                category_name = form.name.data
                cursor.execute('''
                    INSERT INTO categories (category) VALUES (?)
                ''', (category_name,))
                return render_template('new_category_added.html', category=category_name)
        else:
            return redirect(f'/new/category')
    else:
        return render_template('new_category.html', form=form, categories=list_of_categories(app.config.get('DB_URL')))


@app.route('/<category>')
def activity_by_cat(category):
    with get_connection(app.config.get('DB_URL')) as db_connection:
        cursor = db_connection.cursor()
        activities_cursor = cursor.execute('''
            SELECT a.name, a.details, c.category, a.date FROM activities a
            JOIN categories c ON c.id = a.category
            WHERE c.category LIKE ?
        ''', (category,))
        activities = activities_dict(activities_cursor)
        return render_template('activities_list.html', category=f'{category} category', activities=activities)


