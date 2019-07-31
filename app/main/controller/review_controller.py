
from flask import request, g
from flask_restplus import Resource
from flask_restplus.marshalling import marshal

from ..util.dto import ReviewDto, ReviewCreateDto, ReviewDetailDto, ReviewUpdateDto, Review_of_id
from ..service import review_service
from ..util.decorator import admin_token_required, token_required

api = ReviewDto.api
review = ReviewDto.review
review_create = ReviewCreateDto.review
review_detail = ReviewDetailDto.review
review_update = ReviewUpdateDto.review
review_of_id = Review_of_id.review

@api.route("whatever2")
@api.response(404, "no review files have been found")
class ReviewList(Resource):

    @api.doc("list of all review files")
    @token_required
    def get(self):
        review_list = review.service.return_all_review()
        if len(review_list) == 0:
            return {"status": "no review files have been found"}, 404
        return marshal(review_list, review)

    @api.response(201, "review created")
    @api.doc("create new review entry")
    @api.expect(review_create, validate=True)
    def post(self):
        data = request.json
        data["authored_by"] = data['user_id']
        return review_service.create_review(data=data)




@api.route("<review_id>")
@api.param("review_id", "review unique id")
@api.response(404, "review not found")
@api.response(401, "authored_by mismatch")
class review(Resource):

    @api.response(404, "review id not found")
    @api.doc("get a review by id")
    @api.marshal_with(review_detail)
    @token_required
    def get(self, review_id):
        return review_service.return_single_review(review_id)

    @api.doc("update a review by id")
    @api.expect(review_update, validate=True)
    @api.marshal_with(review_update)
    @token_required
    def put(self, review_id):
        data = request.json
        review_id = g
        return review_service.return_single_review(review_id)

    @api.doc("delete review by id")
    @token_required
    def delete(self, review_id):
        if g.user.get("authored_by") != review_service.return_single_review(review_id).authored_by:
            api.abort(401)
        
        return review_service.delete_review(authored_by)

