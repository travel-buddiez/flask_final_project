from flask import g
import uuid

from datetime import datetime

from app.main import db
from app.main.model.tcs_model import Tcs

def create_tcs(data, user):
    try:
        user = user[0].get('data')
        user_id = user.get('user_id')
        new_tcs = Tcs(
            created_on=datetime.utcnow(),
            content=data.get('content'),
            classification=data.get('classification'),
            continent=data.get('continent'),
            authored_by=user_id,
            taboos=data.get('taboos'),
            suggestions=data.get('suggestions'),
            customs=data.get('customs')
        )
        print(new_tcs)
        save_changes(new_tcs)
        response_object = {
            "status": "success",
            "message": "entry created"
        }
        print(response_object)
        return response_object, 201
    except Exception as e:
        response_object = {
            "status": "fail",
            "error": str(e)
        }
        return response_object


def return_all_tcs():
    return Tcs.query.all()


def return_tcs_of_type():
    return Tcs.query.filter_by(classification=classification).all()

def return_tcs_of_continent():
    return Tcs.query.filter_by(continent=continent).all()

def return_tcs_of_country():
    return Tcs.query.filter_by(country=country).all()

def return_tcs_of_state_province():
    return Tcs.query.filter_by(state_province=state_province).all()


def return_single_tcs(id):
    return Tcs.query.filter_by(id=id).first()


def edit_tcs(id, data):
    tcs_to_edit = return_single_tcs(id)
    if tcs:
        for key,item in data.items():
            setattr(tcs, key, item)
        tcs.modified_on = datetime.utcnow()
####work on this        save_changes()
        response = {"status": "updated tcs"}
        return response, 200
    else:
        return {"status": "tcs not found"}, 404

def delete_tcs(id):
    tcs_to_delete = return_single_tcs(id)
    if tcs:
        db.session.delete(tcs)
        db.session.commit()
        return {"status": "no content"}, 204
    else:
        return {"status": "tcs not found"}, 404


def save_changes(data):
    db.session.add(data)
    db.session.commit()
