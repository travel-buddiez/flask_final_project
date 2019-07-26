
from flask import g

from datetime import datetime

from app.main import db
from app.main.model.tcs_model import Tcs

def save_new_tcs(data):
    ###user auth
    if userauth:
        new_tcs = Tcs(
            tcs_id=str(something()),
            created_on=datetime.datetime.utcnow(),
            authored_by=data["db.Foreignkey('user.id')"],
            content=data["content"]
        )
        save_changes(new_tcs)
        response_object = {
            jsonify({
                "status": "success",
                "message": "entry successfully created"
                })
        }
        return response_object, 201
    else:
        response_object = {
            jsonify({
                "status": "fail",
                "message": "how did you get here"
                })
        }
        return response_object, 409


def return_all_tcs():
    return Tcs.query.all()


def return_tcs_of_type():
    return Tcs.query.filter_by(classification=classification).all()


def return_single_tcs(id):
    return Tcs.query.filter_by(id=id).first()


def edit_tcs(id, data):
    tcs_to_edit = return_single_tcs(id)
    if tcs:
        for key,item in data.items():
            setattr(tcs, key, item)
        tcs.modified_on = datetime.utcnow()
        db.session.commit()
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


