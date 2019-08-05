from flask import request, jsonify
from flask_restplus import Resource

from ..util.dto import UserDto
from ..service.user_service import save_new_user, get_all_users, get_a_user

from ..util.decorator import admin_token_required, token_required
from ..model import user
from ..service.auth_helper import Auth

from ..api.continents import testingAPI


api = UserDto.api
_user = UserDto.user

# create a parser for handling Authorization headers
parser = api.parser()
parser.add_argument('Authorization', location='headers')


@api.route('/testing')
class testing(Resource):

    def get(self):
        response_object = {
            'message': testingAPI,
            'Response': 200
        }
        return response_object


@api.route("/me")
class testing(Resource):

    def get(self):
        return (Auth.get_logged_in_user(request))


@api.route('/testing/asia')
class testing(Resource):

    def get(self):
        response_object = {
            "Continent": testingAPI[1],
            "Taboos of Asia": testingAPI[2],
            "Customs of Asia": testingAPI[3],
            "Suggestions for Asia": testingAPI[4],
            'Response': 200
        }
        return response_object


@api.route('/testing/africa')
class testing(Resource):

    def get(self):
        response_object = {
            "Continent": testingAPI[11],
            "Taboos of Africa": testingAPI[12],
            "Customs of Africa": testingAPI[13],
            "Suggestions for Africa": testingAPI[14],
            'Response': 200
        }
        return response_object


@api.route('/testing/europe')
class testing(Resource):

    def get(self):
        response_object = {
            "Continent": testingAPI[16],
            "Taboos of Europe": testingAPI[17],
            "Customs of Europe": testingAPI[18],
            "Suggestions for Europe": testingAPI[19],
            'Response': 200
        }
        return response_object


@api.route('/testing/australia')
class testing(Resource):

    def get(self):
        response_object = {
            "Continent": testingAPI[21],
            "Taboos of Australia": testingAPI[22],
            "Customs of Australia": testingAPI[23],
            "Suggestions for Australia": testingAPI[24],
            'Response': 200
        }
        return response_object


@api.route('/testing/north_america')
class testing(Resource):

    def get(self):
        response_object = {
            "Continent": testingAPI[26],
            "Taboos of North America": testingAPI[27],
            "Customs of North America": testingAPI[28],
            "Suggestions for North America": testingAPI[29],
            'Response': 200
        }
        return response_object


@api.route('/testing/south_america')
class testing(Resource):

    def get(self):
        response_object = {
            "Continent": testingAPI[31],
            "Taboos of South America": testingAPI[32],
            "Customs of South America": testingAPI[33],
            "Suggestions for South America": testingAPI[34],
            'Response': 200
        }
        return response_object


@api.route('/')
@api.response(201, 'User successfully created')
@api.response(409, 'User already exists. Please Log in')
@api.expect(_user, validate=True)
class createUser(Resource):

    def post(self):
        print('hit /')
        '''Creates a new User'''
        data = request.json
        return save_new_user(data=data)


@api.route('/all')
@api.response(200, 'Success')
class UserList(Resource):

    @api.marshal_list_with(_user, envelope='data')
    @api.expect(parser)
    @admin_token_required
    def get(self):
        '''Admin view all registered users'''
        return get_all_users()


@api.route('/<public_id>')
@api.param('public_id', 'The User identifier')
@api.response(404, 'User not found')
class User(Resource):

    @api.marshal_with(_user)
    @api.expect(parser)
    @admin_token_required
    def get(self, public_id):
        '''Admin user lookup'''
        user = get_a_user(public_id)
        if not user:
            api.abort(404)
        else:
            return user


@api.route('/test')
class Test(Resource):

    @api.expect(parser)
    @token_required
    def get(self):
        re = {
            'status': 'How did you get here',
            'message': 'LEAVE'
        }
