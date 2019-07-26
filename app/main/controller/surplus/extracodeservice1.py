
# from datetime import datetime
# from ** import db
# from **.models.surplus.extracode1 import Tcs

# def save_new_tcs(data):
#     ###user auth
#     if userauth:
#         new_tcs = Tcs(
#             tcs_id=str(something()),
#             created_on=datetime.datetime.utcnow(),
#             authored_by=data["db.Foreignkey('users.id')"],
#             text_box=data["text_box"]
#         )
#         save_changes(new_tcs)
#         response_object = {
#             jsonify({
#                 "status": "success",
#                 "message": "entry successfully created"
#                 })
#         }
#         return response_object, 201
#     else:
#         response_object = {
#             jsonify({
#                 "status": "fail",
#                 "message": "how did you get here"
#                 })
#         }
#         return response_object, 409


# def return_all_tcs():
#     return Tcs.query.all()


# def return_tcs_of_type():
#     return Tcs.query.filter_by(class=this).all()


# def return_single_tcs(id):
#     return Tcs.query.filter_by(id=id).first()


# def edit_tcs(id, data):
#     tcs_to_edit = return_single_tcs(id)
#     if tcs:
#         for key,item in data.items():
#             setattr(tcs, key, item)
#         tcs.modified_on = datetime.utcnow()
#         db.session.commit()
#         response = {"status": "updated tcs"}
#         return response, 200
#     else:
#         return {"status": "tcs not found"}, 404

# def delete_tcs(id):
#     tcs_to_delete = return_single_tcs(id)
#     if tcs:
#         db.session.delete(tcs)
#         db.session.commit()
#         return {"status": "no content"}, 204
#     else:
#         return {"status": "tcs not found"}, 404


# def save_changes(data):
#     db.session.add(data)
#     db.session.commit()



# from flask import request, g
# from flask_restplus import Resource
# from flask_restplus.marshalling import marshal

# from ..utils.dto import TcsDto, TcscreateDto, TcsDetailDto, TcsUpdateDto, Tcs_of_id
# from ..services import Tcs_service
# from ..utils.decorator import Authenticate

# api = TcsDto.api
# tcs = TcsDto.tcs
# tcs_create = TcsCreateDto.tcs
# tcs_detail = TcsDetailDto.tcs
# tcs_update = TcsUpdateDto.tcs
# tcs_of_id = Tcs_of_id.tcs

# @api.route("whatever")
# @api.response(404, "no tcs files have been found")
# class TcsList(Resource):

#     @api.doc("list of all tcs files")
#     @Authenticate
#     def get(self):
#         tcs_list = tcs.service.return_all_tcs()
#         if len(tcs_list) == 0:
#             return {"status": "no tcs files have been found"}, 404
#         return marshal(tcs_list, tcs)

#     @api.response(201, "tcs created")
#     @api.doc("create new TCS entry")
#     @api.expect(tcs_create, validate=True)
#     def post(self):
#         data = request.json
#         data["authored_by"] = g.user["authored_by"]
#         return tcs_service.create_tcs(data=data)




# @api.route("<tcs_id>")
# @api.param("tcs_id", "tcs unique id")
# @api.response(404, "Tcs not found")
# @api.response(401, "authored_by mismatch")
# class Tcs(resource):

#     @api.response(404, "Tcs id not found")
#     @api.doc("get a tcs by id")
#     @api.marshal_with(tcs_detail)
#     @Authenticate
#     def get(self, tcs_id):
#         return tcs_service.return_single_tcs(tcs_id)

#     @api.doc("update a tcs by id")
#     @api.expect(tcs_update, validate=True)
#     @api.marshal_with(tcs_update)
#     @Authenticate
#     def put(self, tcs_id):
#         data = request.json
#         tcs_id = g
#         return tcs_service.return_single_tcs(tcs_id)


# from flask_restplus import Api
# from flask import Blueprint

# from .src.controllers.tcs_controller import api as tcs_ns

# tcs_api = Blueprint("api", __name__)

# api = Api(tcs_api,
#         title="Tcs webAPI",
#         version="1.0",
#         description="this is the api for the tcs database"
#     )

# api.add_namespace(tcs.ns, path="/tcs")



# import os

# from flask_migrate import Migrate, MigrateCommand
# from flask_script import Manager

# from ..src import create_tcs, db
# from ..src.models import tcs

# from .. import tcs_api

# app = create_app(os.getenv("FLASK_ENV"))
# app.register_blueprint(tcs_api)

# app.app_context().push()

# manager = Manager(app)

# migrate = Migrate(app, db)

# manager.add_command("db", MigrateCommand)


# @manager.command
# def run():
#     app.run()


# if __name__ == "__main__":
#     manager.run()























# class TcsCreate(Resource):

#     @api.response(201, "Tcs created")
#     @api.doc("create new TCS entry")
#     @api.expect(tcs_create, validate=True)
#     def post(self):
#         data = request.json
#         return tcs_service.create_tcs(data=data)
