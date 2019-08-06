
import datetime
import jwt

from .user import User
from .. import db, flask_bcrypt

class Tcs(db.Model):

    __tablename__ = "tcs"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    classification = db.Column(db.String(50), nullable=False)
    continent = db.Column(db.String(13), nullable=False)
    country = db.Column(db.String(100), nullable=True)
    state_province = db.Column(db.String(100), nullable=True)
    created_on = db.Column(db.DateTime, nullable=False)
    modified_on = db.Column(db.DateTime, nullable=True)
    authored_by = db.Column(db.Integer, nullable=False)
    content = db.Column(db.String(10000), nullable=False)
    customs = db.Column(db.String(10000), nullable=True)
    taboos = db.Column(db.String(10000), nullable=True)
    suggestions = db.Column(db.String(10000), nullable=True)

