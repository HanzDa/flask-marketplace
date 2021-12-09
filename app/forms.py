from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TelField, BooleanField

class SignUpForm(FlaskForm):
    names = StringField(label='Names')
    surnames = StringField(label='Surnames')
    phoneNumber = TelField(label='Phone Number')
    residenceAddress = StringField(label='Residence Address')
    username = StringField(label='Username')
    password = PasswordField(label='Password')
    password2 = PasswordField(label='confirm Password')
    acceptTerms = BooleanField()
    
class LoginForm(FlaskForm):
    username = StringField(label='Username')
    password = PasswordField(label='Password')
    
