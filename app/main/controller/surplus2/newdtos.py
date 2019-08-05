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


class ReviewDto:
    api = Namespace("review", description="review transfer object")
    review = api.model("review", {
      "id": fields.Integer(required=True, description="unique id for individual review object"),
      "authored_by": fields.Integer(required=True, description="the unique user id associated with the review as an author"),
      "created_on": fields.DateTime(description="time of review creation"),
      "tcs_assigned": fields.Integer(required=True, description="the unique id of the tcs file that the is associated with the review")
    })


class ReviewDetailDto:
    review = TcsDto.api.model("tcs_detail", {
      "id": fields.Integer(required=True, description="unique id for individual review object"),
      "authored_by": fields.Integer(required=True, description="the unique user id associated with the review as an author"),
      "created_on": fields.DateTime(description="time of review creation"),
      "modified_on": fields.DateTime(description="time of review modification, if any"),
      "tcs_assigned": fields.Integer(required=True, description="the unique id of the tcs file that the is associated with the review"),
      "content": fields.String(required=False, description="content of the review"),
      "rating": fields.Integer(required=True, description="the rating/review of the review object for the tcs")
    })


class Review_of_id:
    review = TcsDto.api.model("tcs_detail", {
      "id": fields.Integer(required=True, description="unique id for individual review object"),
      "authored_by": fields.Integer(required=True, description="the unique user id associated with the review as an author"),
      "created_on": fields.DateTime(description="time of review creation"),
      "modified_on": fields.DateTime(description="time of review modification, if any"),
      "tcs_assigned": fields.Integer(required=True, description="the unique id of the tcs file that the is associated with the review"),
      "content": fields.String(required=False, description="content of the review"),
      "rating": fields.Integer(required=True, description="the rating/review of the review object for the tcs")
    })


class ReviewCreateDto:
    review = TcsDto.api.model("tcs_create", {
      "content": fields.String(required=False, description="content of the review"),
      "rating": fields.Integer(required=True, description="the rating/review of the review object for the tcs")
    })

class ReviewUpdateDto:
    review = TcsDto.api.model("tcs_update", {
      "content": fields.String(required=False, description="content of the review"),
      "rating": fields.Integer(required=True, description="the rating/review of the review object for the tcs")
    })
