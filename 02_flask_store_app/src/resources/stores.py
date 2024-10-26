import uuid
from flask import request
from flask_smorest import Blueprint, abort
from flask.views import MethodView
from db import stores
from schema import StoreSchema

blp = Blueprint("Stores", __name__, description="Operations on Stores")

@blp.route("/store/<string:store_id>")
class StoreControllerOne(MethodView):

  @blp.response(200, StoreSchema)
  def get(self, store_id):
    try:
      return stores[store_id]
    except KeyError:
      abort(404, message="Store not found.")

  def delete(self, store_id):
    try:
      del stores[store_id]
      return {"message":"Store deleted"}, 200
    except KeyError:
      abort(404, message="Store not found.")


@blp.route("/store")
class StorecontrollerTwo(MethodView):

  @blp.response(200, StoreSchema(many=True))
  def get(self):
    return stores.values()

  @blp.arguments(StoreSchema)
  @blp.response(201, StoreSchema)
  def post(self, store_data):
    for store in stores.values():
      if store["name"] == store_data["name"]:
        abort(409, message="The store is already exists.")
    store_id = uuid.uuid4().hex
    store = {**store_data, "id": store_id}
    stores[store_id] = store
    return store

