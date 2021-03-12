"""Forms for adopt app."""
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired, Optional

class AddPetForm(FlaskForm):
    name = StringField('Pet name', validators = [InputRequired()])
    species = StringField('Species', validators = [InputRequired()])
    photo_url = StringField('Photo URL')
    age = StringField('Age', validators = [InputRequired()])
    notes = StringField('Notes', validators = [Optional()])