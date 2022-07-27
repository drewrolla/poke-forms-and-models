from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class UserCreationForm(FlaskForm):
    poke_name = StringField('Pokemon Name', validators=[DataRequired()])
    submit = SubmitField()