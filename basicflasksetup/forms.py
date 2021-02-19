from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from basicflasksetup.models import User

class SignupForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')




