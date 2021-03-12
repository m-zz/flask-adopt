"""Models for adopt app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    """Connect this database to provided Flask app.

    You should call this in your Flask app.
    """

    db.app = app
    db.init_app(app)

class Pet(db.Model):

    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.Text, nullable = False)
    species = db.Column(db.Text, nullable = False)
    photo_url = db.Column(db.Text, nullable = False, default = 'https://lh3.googleusercontent.com/proxy/dP96VkXkYuym6Gma1wwXiOQXwPsk5JdzhV3X07KCVhMxMmzqoVmxlXPOAfeKz6Un7TdtDbyc-2yVVlGVuI3ZWNgff58M_pMCGgbHE4nSu9u7otfSPj1OZUmYwbbp0xiseQt_jCX0zgwV4HFW')
    age = db.Column(db.Text, nullable = False)
    # how to check within list
    notes = db.Column(db.Text) 
    # do we need to specify nullable
    available = db.Column(db.Boolean, nullable = False, default = True)
    # True or true

    