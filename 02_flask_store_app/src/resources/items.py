import uuid
from flask import request
from flask.views import MethodView
from flask_smorest  import Blueprint, abort
from db import items
from schema import ItemSchema, ItemUpdateSchema

blp = Blueprint("Items", __name__, description="Operations on Items")

@blp.route("/item/<string:item_id>")
class ItemsControllerOne(MethodView):

  @blp.response(200, ItemSchema)
  def get(self, item_id):
    try:
      return items[item_id]
    except KeyError:
      abort(404, message="Item not found.")

  @blp.arguments(ItemUpdateSchema)
  @blp.response(200, ItemSchema)
  def update(self, item_data, item_id):
    item = None
    try:
      item = items[item_id]
    except KeyError:
      abort(400, message="Item not found.")
    item |= item_data
    return item, 200

  def delete(self, item_id):
    try:
      del items[item_id]
      return {"message":"Item deleted"}, 200
    except KeyError:
      abort(404, message="Item not found.")


@blp.route("/item")
class ItemsControllerTwo(MethodView):

  @blp.response(200, ItemSchema(many=True))
  def get(self):
    return items.values()

  @blp.arguments(ItemSchema)
  @blp.response(201, ItemSchema)
  def post(self, item_data):
    for item in items.values():
      if item["name"] == item_data['name']:
        abort(409, message="The item already exists.")
    item_id = uuid.uuid4().hex
    item = {**item_data, "id":item_id}
    items[item_id] = item
    return item
