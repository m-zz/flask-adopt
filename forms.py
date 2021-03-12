"""Forms for adopt app."""
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
from wtforms.validators import InputRequired, Optional, URL, AnyOf

class AddPetForm(FlaskForm):
    name = StringField('Pet name', validators = [InputRequired()])
    species = StringField('Species', validators = [InputRequired(), AnyOf(["cat", "dog", "porcupine"])])
    photo_url = StringField('Photo URL', validators= [URL()])
    age = StringField('Age', validators = [InputRequired(), AnyOf(["baby", "young", "adult", "senior"])])
    notes = StringField('Notes', validators = [Optional()])
    available = BooleanField("Available")