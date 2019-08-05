
import datetime
import jwt

from .user import User
from .. import db, flask_bcrypt

class Tcs(db.Model):

    __tablename__ = "tcs"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    classification = db.Column(db.String(10), nullable=False)
    continent = db.Column(db.String(13), nullable=False)
    country = db.Column(db.String(100), nullable=True)
    state_province = db.Column(db.String(100), nullable=True)
    created_on = db.Column(db.DateTime, nullable=False)
    modified_on = db.Column(db.DateTime, nullable=True)
<<<<<<< HEAD
    authored_by = db.Column(db.ForeignKey("user.id"), nullable=False)
    content = db.Column(db.String(10000), nullable=False)

=======
    authored_by = db.Column(db.Integer, nullable=False)
    content = db.Column(db.String(10000), nullable=False)
>>>>>>> 370fa97b7bcdc47bb8c69c5c2da232bae0cd4a7e
