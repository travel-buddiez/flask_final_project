from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'admin': fields.Boolean(required=False, description='Set user admin privilages'),
    })

class UserUpdateDto:
    user_update = UserDto.api.model("user_update", {
      'username': fields.String(required=True, description='user username'),
      'email': fields.String(required=True, description='user email'),
      'bio': fields.String(required=True, description='user bio'),
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
      "classification": fields.String(required=True, description="the classification of Tabboo, Custom, or Suggestion"),
      "continent": fields.String(required=True, description="the continent of the tcs object"),
      "content": fields.String(required=True, description="content of the tcs"),
    })


class TcsDetailDto:
    tcs = TcsDto.api.model("tcs_detail", {
      "id": fields.Integer(required=True, description="unique id for individual tcs object"),
      "authored_by": fields.Integer(required=True, description="the unique user id associated with the tcs as an author"),
      "created_on": fields.DateTime(description="time of tcs creation"),
      "modified_on": fields.DateTime(description="time of tcs modification, if any"),
      "content": fields.String(required=True, description="content of the tcs"),
      "classification": fields.String(required=True, description="the classification of Tabboo, Custom, or Suggestion"),
      "continent": fields.String(required=True, description="the continent of the tcs object"),
      "country": fields.String(required=False, description="the continent of the tcs object"),
      "state/province": fields.String(required=False, description="the continent of the tcs object")
    })


class Tcs_of_id:
    tcs = TcsDto.api.model("tcs_detail", {
      "id": fields.Integer(required=True, description="unique id for individual tcs object"),
      "authored_by": fields.Integer(required=True, description="the unique user id associated with the tcs as an author"),
      "created_on": fields.DateTime(description="time of tcs creation"),
      "modified_on": fields.DateTime(description="time of tcs modification, if any"),
      "content": fields.String(required=True, description="content of the tcs"),
      "classification": fields.String(required=True, description="the classification of Tabboo, Custom, or Suggestion"),
      "continent": fields.String(required=True, description="the continent of the tcs object"),
      "country": fields.String(required=False, description="the continent of the tcs object"),
      "state/province": fields.String(required=False, description="the continent of the tcs object")
    })


class TcsCreateDto:
    tcs = TcsDto.api.model("tcs_create", {
      "content": fields.String(required=True, description="content of the tcs"),
      "classification": fields.String(required=True, description="the classification of Tabboo, Custom, or Suggestion"),
      "continent": fields.String(required=True, description="the continent of the tcs object")
    })

class TcsUpdateDto:
    tcs = TcsDto.api.model("tcs_update", {
      "content": fields.String(required=True, description="content of the tcs"),
      "classification": fields.String(required=True, description="the classification of Tabboo, Custom, or Suggestion"),
      "continent": fields.String(required=True, description="the continent of the tcs object")
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
    review = ReviewDto.api.model("review_detail", {
      "id": fields.Integer(required=True, description="unique id for individual review object"),
      "authored_by": fields.Integer(required=True, description="the unique user id associated with the review as an author"),
      "created_on": fields.DateTime(description="time of review creation"),
      "modified_on": fields.DateTime(description="time of review modification, if any"),
      "tcs_assigned": fields.Integer(required=True, description="the unique id of the tcs file that the is associated with the review"),
      "content": fields.String(required=False, description="content of the review"),
      "rating": fields.Integer(required=True, description="the rating/review of the review object for the tcs")
    })


class Review_of_id:
    review = ReviewDto.api.model("review_detail", {
      "id": fields.Integer(required=True, description="unique id for individual review object"),
      "authored_by": fields.Integer(required=True, description="the unique user id associated with the review as an author"),
      "created_on": fields.DateTime(description="time of review creation"),
      "modified_on": fields.DateTime(description="time of review modification, if any"),
      "tcs_assigned": fields.Integer(required=True, description="the unique id of the tcs file that the is associated with the review"),
      "content": fields.String(required=False, description="content of the review"),
      "rating": fields.Integer(required=True, description="the rating/review of the review object for the tcs")
    })


class ReviewCreateDto:
    review = ReviewDto.api.model("review_create", {
      "content": fields.String(required=False, description="content of the review"),
      "rating": fields.Integer(required=True, description="the rating/review of the review object for the tcs")
    })

class ReviewUpdateDto:
    review = ReviewDto.api.model("review_update", {
      "content": fields.String(required=False, description="content of the review"),
      "rating": fields.Integer(required=True, description="the rating/review of the review object for the tcs")
    })
