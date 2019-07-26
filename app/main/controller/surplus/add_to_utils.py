
class TcsDto:
    api = Namespace("tcs", description="tcs transfer object")
    tcs = api.model("tcs", {
      "id": fields.Integer(required=True, description="unique id for individual tcs object")
      "authored_by": fields.Integer(required=True, description="the unique user id associated with the tcs as an author")
      "created_on": fields.DateTime(description="time of tcs creation")
      "classification": fields.String(required=True, description="the classification of Tabboo, Custom, or Suggestion")
    })


class TcsDetailDto:
    tcs = TcsDto.api.model("tcs_detail", {
      "id": fields.Integer(required=True, description="unique id for individual tcs object"),
      "authored_by": fields.Integer(required=True, description="the unique user id associated with the tcs as an author")
      "created_on": fields.DateTime(description="time of tcs creation"),
      "modified_on": fields.DateTime(description="time of tcs modification, if any"),
      "content": fields.String(required=True, description="content of the tcs")
      "classification": fields.String(required=True, description="the classification of Tabboo, Custom, or Suggestion")
    })


class Tcs_of_id:
    tcs = TcsDto.api.model("tcs_detail", {
      "id": fields.Integer(required=True, description="unique id for individual tcs object"),
      "authored_by": fields.Integer(required=True, description="the unique user id associated with the tcs as an author")
      "created_on": fields.DateTime(description="time of tcs creation"),
      "modified_on": fields.DateTime(description="time of tcs modification, if any")
      "content": fields.String(required=True, description="content of the tcs")
      "classification": fields.String(required=True, description="the classification of Tabboo, Custom, or Suggestion")
    })


class TcsCreateDto:
    tcs = TcsDto.api.model("tcs_create", {
      "content": fields.String(required=True, description="content of the tcs")
      "classification": fields.String(required=True, description="the classification of Tabboo, Custom, or Suggestion")
    })

class TcsUpdateDto:
    tcs = TcsDto.api.model("tcs_update", {
      "content": fields.String(required=True, description="content of the tcs")
      "classification": fields.String(required=True, description="the classification of Tabboo, Custom, or Suggestion")
    })
