from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from flask_wtf import FlaskForm
from wtforms import TimeField, IntegerField, StringField
from wtforms.validators import DataRequired, Optional


# Create the form for the show input
class ShowForm(FlaskForm):
    show_name = StringField('Show Name', validators=[DataRequired()])
    start_time = TimeField('Start Time', validators=[DataRequired()])
    end_time = TimeField('End Time', validators=[DataRequired()])
    rating = IntegerField('Rating', validators=[Optional()])
    tags = StringField('Tags', validators=[Optional()])
    show_price = IntegerField('Price', validators=[DataRequired()])
