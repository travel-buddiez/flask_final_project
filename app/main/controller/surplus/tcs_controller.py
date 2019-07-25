
from flask import request, g
from flask_restplus import Resource
from flask_restplus.marshalling import marshal

from ..util.dto import TcsDto, TcscreateDto, TcsDetailDto, TcsUpdateDto, Tcs_of_id
from ..services import Tcs_service
from ..util.decorator import Authenticate

api = TcsDto.api
tcs = TcsDto.tcs
tcs_create = TcsCreateDto.tcs
tcs_detail = TcsDetailDto.tcs
tcs_update = TcsUpdateDto.tcs
tcs_of_id = Tcs_of_id.tcs

@api.route("whatever")
@api.response(404, "no tcs files have been found")
class TcsList(Resource):

    @api.doc("list of all tcs files")
    @Authenticate
    def get(self):
        tcs_list = tcs.service.return_all_tcs()
        if len(tcs_list) == 0:
            return {"status": "no tcs files have been found"}, 404
        return marshal(tcs_list, tcs)

    @api.response(201, "tcs created")
    @api.doc("create new TCS entry")
    @api.expect(tcs_create, validate=True)
    def post(self):
        data = request.json
        data["authored_by"] = g.user["authored_by"]
        return tcs_service.create_tcs(data=data)




@api.route("<tcs_id>")
@api.param("tcs_id", "tcs unique id")
@api.response(404, "Tcs not found")
@api.response(401, "authored_by mismatch")
class Tcs(resource):

    @api.response(404, "Tcs id not found")
    @api.doc("get a tcs by id")
    @api.marshal_with(tcs_detail)
    @Authenticate
    def get(self, tcs_id):
        return tcs_service.return_single_tcs(tcs_id)

    @api.doc("update a tcs by id")
    @api.expect(tcs_update, validate=True)
    @api.marshal_with(tcs_update)
    @Authenticate
    def put(self, tcs_id):
        data = request.json
        tcs_id = g
        return tcs_service.return_single_tcs(tcs_id)

    @api.doc("delete tcs by id")
    @Authenticate
    def delete(self, tcs_id):
        if g.user.get("authored_by") != tcs_service.return_single_tcs(tcs_id).authored_by:
            api.abort(401)
        
        return tcs_service.delete_tcs(authored_by)

