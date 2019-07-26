
import datetime
import jwt

from .user import User
from .. import db, flask_bcrypt

class Tcs(db.Model):

    __tablename__ = "tcs"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    classification = db.Column(db.String(10), nullable=False)
    created_on = db.Column(db.DateTime, nullable=False)
    modified_on = db.Column(db.DateTime, nullable=True)
    authored_by = db.Column(db.ForeignKey("users.id"), nullable=False)
    content = db.Column(db.String(10000), nullable=False)

