
from flask import g

from datetime import datetime

from app.main import db
from app.main.model.review_model import Review

def save_new_review(data):
    ###user auth
    if userauth:
        new_review = Review(
            review_id=str(something()),
            created_on=datetime.datetime.utcnow(),
            authored_by=data["db.Foreignkey('user.id')"],
            tcs_assigned=data["db.Foreignkey('tcs.id')"],
            rating=data["rating"],
            content=data["content"]
        )
        save_changes(new_review)
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


def return_all_review():
    return Review.query.all()


def return_review_of_type():
    return review.query.filter_by(tcs_assigned=tcs_assigned).all()


def return_single_review(id):
    return review.query.filter_by(id=id).first()


def edit_review(id, data):
    review_to_edit = return_single_review(id)
    if review:
        for key,item in data.items():
            setattr(review, key, item)
        review.modified_on = datetime.utcnow()
        db.session.commit()
        response = {"status": "updated review"}
        return response, 200
    else:
        return {"status": "review not found"}, 404

def delete_review(id):
    review_to_delete = return_single_review(id)
    if review:
        db.session.delete(review)
        db.session.commit()
        return {"status": "no content"}, 204
    else:
        return {"status": "review not found"}, 404


def save_changes(data):
    db.session.add(data)
    db.session.commit()


