from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length


class HuntButtomForm(FlaskForm):
    submit = SubmitField('Submit')