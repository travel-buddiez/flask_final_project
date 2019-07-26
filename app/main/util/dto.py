from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'admin': fields.Boolean(required=False, description='Set user admin privilages'),
    })


class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password')
    })


class TcsDto:
    api = Namespace("tcs", description="tcs transfer object")
    tcs = api.model("tcs", {
      "id": fields.Integer(required=True, description="unique id for individual tcs object"),
      "authored_by": fields.Integer(required=True, description="the unique user id associated with the tcs as an author"),
      "created_on": fields.DateTime(description="time of tcs creation"),
      "classification": fields.String(required=True, description="the classification of Tabboo, Custom, or Suggestion")
    })


class TcsDetailDto:
    tcs = TcsDto.api.model("tcs_detail", {
      "id": fields.Integer(required=True, description="unique id for individual tcs object"),
      "authored_by": fields.Integer(required=True, description="the unique user id associated with the tcs as an author"),
      "created_on": fields.DateTime(description="time of tcs creation"),
      "modified_on": fields.DateTime(description="time of tcs modification, if any"),
      "content": fields.String(required=True, description="content of the tcs"),
      "classification": fields.String(required=True, description="the classification of Tabboo, Custom, or Suggestion")
    })


class Tcs_of_id:
    tcs = TcsDto.api.model("tcs_detail", {
      "id": fields.Integer(required=True, description="unique id for individual tcs object"),
      "authored_by": fields.Integer(required=True, description="the unique user id associated with the tcs as an author"),
      "created_on": fields.DateTime(description="time of tcs creation"),
      "modified_on": fields.DateTime(description="time of tcs modification, if any"),
      "content": fields.String(required=True, description="content of the tcs"),
      "classification": fields.String(required=True, description="the classification of Tabboo, Custom, or Suggestion")
    })


class TcsCreateDto:
    tcs = TcsDto.api.model("tcs_create", {
      "content": fields.String(required=True, description="content of the tcs"),
      "classification": fields.String(required=True, description="the classification of Tabboo, Custom, or Suggestion")
    })

class TcsUpdateDto:
    tcs = TcsDto.api.model("tcs_update", {
      "content": fields.String(required=True, description="content of the tcs"),
      "classification": fields.String(required=True, description="the classification of Tabboo, Custom, or Suggestion")
    })
