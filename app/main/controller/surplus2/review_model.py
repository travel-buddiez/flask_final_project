
import datetime
import jwt

from .tcs import Tcs
from .user import User
from .. import db, flask_bcrypt

class Review(db.Model):

    __tablename__ = "review"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tcs_assigned = db.Column(db.ForeignKey("tcs.id"), nullable=False)
    rating = db.Column(db.integer, nullable=False)
    created_on = db.Column(db.DateTime, nullable=False)
    modified_on = db.Column(db.DateTime, nullable=True)
    authored_by = db.Column(db.ForeignKey("users.id"), nullable=False)
    content = db.Column(db.String(10000), nullable=True)

