from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired
from db import list_of_categories
from app import app


class NewActivityForm(FlaskForm):
    name = StringField('Activity name', validators=[DataRequired()])
    details = StringField('Details')
    category = SelectField('Category', validators=[DataRequired()], choices=list_of_categories(app.config.get('DB_URL')))
    date = StringField('Due date')
    add = SubmitField('Add activity')


class NewCategoryForm(FlaskForm):
    name = StringField('Category name', validators=[DataRequired()])
    add = SubmitField('Add category')