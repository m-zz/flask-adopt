"""Flask app for adopt app."""

from flask import Flask, render_template, redirect, request

from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Pet

from forms import AddPetForm

from project_secrets import PETFINDER_API_KEY, PETFINDER_SECRET_KEY

import requests

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

connect_db(app)
db.drop_all()
db.create_all()

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
AUTH_URL = "https://api.petfinder.com/v2/oauth2/token"

a = Pet(name= "Nelly", species= "dog", age="baby")
db.session.add(a)
db.session.commit()

auth_token = None

@app.before_first_request
def refresh_credentials():
    """Just once, get token and store it globally."""
    global auth_token
    auth_token = update_auth_token_string()

def update_auth_token_string():
    resp = requests.post(AUTH_URL, data = {"grant_type": "client_credentials",
    "client_id": PETFINDER_API_KEY, "client_secret": PETFINDER_SECRET_KEY})
    return resp.json()["access_token"]

@app.route('/')
def show_pets():
    
    pets = Pet.query.all()
    return render_template('pets.html', pets = pets)

@app.route('/add', methods = ["GET", "POST"])
def add_pet():
    form = AddPetForm()

    if form.validate_on_submit():
        new_pet = Pet(name = form.name.data, species = form.species.data, photo_url = form.photo_url.data,
        age = form.age.data, notes = form.notes.data)
        db.session.add(new_pet)
        db.session.commit()

        return redirect('/')

    return render_template('add_pet.html', form = form)
    
@app.route('/<int:pet_id>', methods = ["GET", "POST"])
def edit_pet(pet_id):

    pet = Pet.query.get_or_404(pet_id)
    form = AddPetForm(obj=pet)

    if form.validate_on_submit():
        print(pet.photo_url, pet.notes, pet.available)
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        
        db.session.commit()

        return redirect('/')

    return render_template("edit_pet.html", form = form, pet=pet)
    
