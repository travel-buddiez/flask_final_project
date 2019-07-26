
# import datetime
# import jwt

# from .user import User
# from .. import db, bcrypt

# class Tcs(db.Model):

#     __tablename__ = "tcs"

#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     ### one of 3 classes?
#     created_on = db.Column(db.DateTime, nullable=False)
#     modified_on = db.Column(db.DateTime, nullable=True)
#     authored_by = db.Column(db.Foreignkey("users.id"), nullable=False)
#     text_box = db.Column(db.String(10000), nullable=False)


# class TcsDto:
#     api = Namespace("tcs", description="tcs transfer object")
#     tcs = api.model("tcs", {
#       "id": fields.Integer(required=True, description="unique id for individual tcs object")
#       "authored_by": #pull foreign username key,
#       "created_on": fields.DateTime(description="time of tcs creation")
#     })


# class TcsDetailDto:
#     tcs = TcsDto.api.model("tcs_detail", {
#       "id": fields.Integer(required=True, description="unique id for individual tcs object"),
#       "authored_by": ,#pull foreign username key,
#       "created_on": fields.DateTime(description="time of tcs creation"),
#       "modified_on": fields.DateTime(description="time of tcs modification, if any"),
#       "content": fields.String(required=True, description="content of the tcs")
#     })


# class Tcs_of_id:
#     tcs = TcsDto.api.model("tcs_detail", {
#       "id": fields.Integer(required=True, description="unique id for individual tcs object"),
#       "authored_by": ,#pull foreign username key,
#       "created_on": fields.DateTime(description="time of tcs creation"),
#       "modified_on": fields.DateTime(description="time of tcs modification, if any")
#       "text_box": fields.String(required=True, description="contains the string of written text for the tcs")
#     })


# class TcsCreateDto:
#     tcs = TcsDto.api.model("tcs_create", {
#       "content": fields.String(required=True, description="content of the tcs")
#     })

# class TcsUpdateDto:
#     tcs = TcsDto.api.model("tcs_update", {
#       "content": fields.String(required=True, description="content of the tcs")
#     })







# class TcsUpdateDto:
#     tcs = TcsDto.api.model("tcs_update", {
#       "id": fields.Integer(required=True, description="unique id for individual tcs object"),
#       "authored_by": ,#pull foreign username key,
#     })






# class TcsCreateDto:
#     tcs = TcsDto.api.model("tcs_create", {
#       "id": fields.Integer(required=True, description="unique id for individual tcs object"),
#       "authored_by": ,#pull foreign username key,
#       "created_on": fields.DateTime(required=True, description="time of tcs creation"),
#       "modified_on": fields.DateTime(required=False, description="time of tcs modification, if any")
#       "content": fields.String(required=True, description="content of the tcs")
#       "text_box": fields.String(required=True, description="contains the string of written text for the tcs")
#     })