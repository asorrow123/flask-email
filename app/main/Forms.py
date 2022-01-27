from flask_wtf import FlaskForm
from wtforms import StringField

class EmailForm(FlaskForm):
    recipient = StringField('to')
    subject = StringField('subject')
    body = StringField('message')
