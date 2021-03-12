"""Forms for adopt app."""
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
from wtforms.validators import InputRequired, Optional, URL, AnyOf

class AddPetForm(FlaskForm):
    name = StringField('Pet name', validators = [])
    species = StringField('Species', validators = [AnyOf(["cat", "dog", "porcupine"])])
    photo_url = StringField('Photo URL', validators= [Optional()])
    age = StringField('Age', validators = [AnyOf(["baby", "young", "adult", "senior"])])
    notes = StringField('Notes', validators = [Optional()])
    available = BooleanField("Available")

# in solution, there was a separate EditPetForm with correct validators 
# to prevent issue with InputRequired() and filtering form fields