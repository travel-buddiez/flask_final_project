
from flask import request, g
from flask_restplus import Resource
from flask_restplus.marshalling import marshal

from ..util.dto import TcsDto, TcsCreateDto, TcsDetailDto, TcsUpdateDto, Tcs_of_id
from ..service import tcs_service
from ..util.decorator import admin_token_required, token_required

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
    @token_required
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
class Tcs(Resource):

    @api.response(404, "Tcs id not found")
    @api.doc("get a tcs by id")
    @api.marshal_with(tcs_detail)
    @token_required
    def get(self, tcs_id):
        return tcs_service.return_single_tcs(tcs_id)

    @api.doc("update a tcs by id")
    @api.expect(tcs_update, validate=True)
    @api.marshal_with(tcs_update)
    @token_required
    def put(self, tcs_id):
        data = request.json
        tcs_id = g
        return tcs_service.return_single_tcs(tcs_id)

    @api.doc("delete tcs by id")
    @token_required
    def delete(self, tcs_id):
        if g.user.get("authored_by") != tcs_service.return_single_tcs(tcs_id).authored_by:
            api.abort(401)
        
        return tcs_service.delete_tcs(authored_by)


@api.route("filter_continent")
@api.response(404, "no tcs files have been found")
class TcsListFilter(Resource):

    @api.doc("list of continent_filtered tcs files")
    @token_required
    def get(self):
        tcs_continent_filtered_list = tcs.service.return_tcs_of_continent()
        if len(tcs_continent_filtered_list) == 0:
            return {"status": "no tcs files have been found"}, 404
        return marshal(tcs_continent_filtered_list, tcs)


@api.route("filter_country")
@api.response(404, "no tcs files have been found")
class TcsListFilterCountry(Resource):

    @api.doc("list of country_filtered tcs files")
    @token_required
    def get(self):
        tcs_country_filtered_list = tcs.service.return_tcs_of_country()
        if len(tcs_country_filtered_list) == 0:
            return {"status": "no tcs files have been found"}, 404
        return marshal(tcs_country_filtered_list, tcs)


@api.route("filter_state_province")
@api.response(404, "no tcs files have been found")
class TcsListFilterState_Province(Resource):

    @api.doc("list of state_province_filtered tcs files")
    @token_required
    def get(self):
        tcs_state_province_filtered_list = tcs.service.return_tcs_of_state_province()
        if len(tcs_state_province_filtered_list) == 0:
            return {"status": "no tcs files have been found"}, 404
        return marshal(tcs_state_province_filtered_list, tcs)