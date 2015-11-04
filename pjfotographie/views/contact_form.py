'''
WTForms implementation.
'''
from flask_wtf import Form
from flask_wtf.html5 import TelField, EmailField
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Length, Regexp


class ContactForm(Form):
    '''
    Form class for WTForms usage.
    '''
    name = StringField('name', validators=[DataRequired(), Length(min=3)])
    phone = TelField('phone', validators=[DataRequired(),
                                          Regexp("^[0-9]{10}$")])
    email = EmailField('email', validators=[DataRequired()])
    message = TextAreaField('message')
