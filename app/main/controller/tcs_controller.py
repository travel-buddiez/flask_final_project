
from flask import request, g
from flask_restplus import Resource
from flask_restplus.marshalling import marshal

from ..util.dto import TcsDto, TcsCreateDto, TcsDetailDto, TcsUpdateDto, Tcs_of_id, UserDto
from ..service.tcs_service import create_tcs, return_all_tcs, return_tcs_of_type, return_tcs_of_continent, return_tcs_of_country, return_tcs_of_state_province, return_single_tcs, edit_tcs, delete_tcs
from ..service import tcs_service
from ..util.decorator import admin_token_required, token_required
from ..service.auth_helper import Auth

api = TcsDto.api
tcs = TcsDto.tcs
tcsCreate = TcsCreateDto.tcs
tcsDetail = TcsDetailDto.tcs
tcsUpdate = TcsUpdateDto.tcs
tcs_of_id = Tcs_of_id.tcs


user_api = UserDto.api
parser = user_api.parser()
parser.add_argument('Authorization', location='headers')


@api.route("/whatever")
@api.response(404, "no tcs files have been found")
class TcsList(Resource):

    @api.doc("list of all tcs files")
    @api.marshal_list_with(tcs, envelope='data')
#    @token_required
    @api.expect(parser)
    def get(self):
        tcs_list = return_all_tcs()
        print("I'm Here")
        if len(tcs_list) == 0:
            return {"status": "no tcs files have been found"}, 404
        print(tcs_list)
        return tcs_list

    @api.doc("create new TCS entry")
    @api.expect(parser)
    @api.expect(tcsCreate, validate=True)
    def post(self):
        data = request.json
        auth_token = request.headers.get('Authorization')
        user = Auth.get_logged_in_user(auth_token)
        return create_tcs(data, user)



@api.route("/<tcs_id>")
@api.param("tcs_id", "tcs unique id")
@api.response(404, "Tcs not found")
@api.response(401, "authored_by mismatch")
class Tcs(Resource):

    @api.response(404, "Tcs id not found")
    @api.doc("get a tcs by id")
    @api.marshal_with(tcsDetail)
#    @token_required
    def get(self, tcs_id):
        print("here++++++++++++++")
        return return_single_tcs(tcs_id)
#=================================================================================================================================================
    @api.doc("update a tcs by id")
    @api.expect(parser)
    @api.expect(tcsUpdate, validate=True)
    def put(self, tcs_id):
        data = request.json
        auth_token = request.headers.get('Authorization')
        user = Auth.get_logged_in_user(auth_token)
        print('got here')
        return edit_tcs(tcs_id, data, user)
#==================================================================================================================================================
    @api.doc("delete tcs by id")
    @api.marshal_with(tcsDetail)
#    @token_required
    def delete(self, tcs_id):
        auth_token = request.headers.get('Authorization')
        return tcs_service.delete_tcs(tcs_id, auth_token)


@api.route("/filter_continent")
@api.response(404, "no tcs files have been found")
class TcsListFilter(Resource):

    @api.doc("list of continent_filtered tcs files")
    @token_required
    def get(self):
        tcs_continent_filtered_list = tcs.service.return_tcs_of_continent()
        if len(tcs_continent_filtered_list) == 0:
            return {"status": "no tcs files have been found"}, 404
        return marshal(tcs_continent_filtered_list, tcs)


@api.route("/filter_country")
@api.response(404, "no tcs files have been found")
class TcsListFilterCountry(Resource):

    @api.doc("list of country_filtered tcs files")
    @token_required
    def get(self):
        tcs_country_filtered_list = tcs.service.return_tcs_of_country()
        if len(tcs_country_filtered_list) == 0:
            return {"status": "no tcs files have been found"}, 404
        return marshal(tcs_country_filtered_list, tcs)


@api.route("/filter_state_province")
@api.response(404, "no tcs files have been found")
class TcsListFilterState_Province(Resource):

    @api.doc("list of state_province_filtered tcs files")
    @token_required
    def get(self):
        tcs_state_province_filtered_list = tcs.service.return_tcs_of_state_province()
        if len(tcs_state_province_filtered_list) == 0:
            return {"status": "no tcs files have been found"}, 404
        return marshal(tcs_state_province_filtered_list, tcs)
