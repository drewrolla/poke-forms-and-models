from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired

class PokemonSearchForm(FlaskForm):
    poke_name = StringField('Pokemon Name', validators=[InputRequired()])
    submit = SubmitField()
    # save Pokemon to db
    catch = SubmitField()
    run = SubmitField()