from flask_smorest import Blueprint, abort
from flask.views import MethodView
from schema import StoreSchema
from db import db
from models import StoreModel
from sqlalchemy.exc import SQLAlchemyError


blp = Blueprint("Stores", __name__, description="Operations on Stores")

@blp.route("/store/<string:store_id>")
class StoreControllerOne(MethodView):

  @blp.response(200, StoreSchema)
  def get(self, store_id):
    store = StoreModel.query.get_or_404(store_id)
    return store

  def delete(self, store_id):
    store = StoreModel.query.get_or_404(store_id)
    db.session.delete(store)
    db.session.commit()
    return {"message":"Store deleted"}, 200


@blp.route("/store")
class StoreControllerTwo(MethodView):

  @blp.response(200, StoreSchema(many=True))
  def get(self):
    return StoreModel.query.all()

  @blp.arguments(StoreSchema)
  @blp.response(201, StoreSchema)
  def post(self, store_data):
    store = None
    try:
        store = StoreModel(**store_data)
        db.session.add(store)
        db.session.commit()
    except SQLAlchemyError:
      abort(500, message="Error occured while insert store data")
    except Exception as e:
      print(e)
    return store

