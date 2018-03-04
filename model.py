from datetime import datetime
import hashlib
from werkzeug.security import generate_password_hash, check_password_hash
from flask import current_app, request, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, AnonymousUserMixin

db = SQLAlchemy()

#############################################
# Model definitions

class User(db.Model):
    """ Contains user information. """

    __tablename__ = 'user'

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    def __repr__(self):

        return "<User user_id={} email={}".format(self.user_id, self.email)

#############################################

def connect_to_db(app):
    """ Connect the database to the Flask app. """

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///mitrc'
    app.config['SQLALCHEMY_ECHO'] = True
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    from server import app
    connect_to_db(app)
    print "Connected to DB."
