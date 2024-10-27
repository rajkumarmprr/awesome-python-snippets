from flask.views import MethodView
from flask_smorest  import Blueprint, abort
from schema import ItemSchema, ItemUpdateSchema
from db import db
from models import ItemModel
from sqlalchemy.exc import SQLAlchemyError

blp = Blueprint("Items", __name__, description="Operations on Items")

@blp.route("/item/<string:item_id>")
class ItemsControllerOne(MethodView):

  @blp.response(200, ItemSchema)
  def get(self, item_id):
      item = ItemModel.query.get_or_404(item_id)
      return item

  @blp.arguments(ItemUpdateSchema)
  @blp.response(200, ItemSchema)
  def update(self, item_data, item_id):
    item = ItemModel.query.get_or_404(item_id)
    item.name = item_data.get("name")
    item.price = item_data.get("price")
    db.session.add(item)
    db.session.commit()
    return item, 200

  def delete(self, item_id):
    item = ItemModel.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    return {"message":"Item deleted"}, 200



@blp.route("/item")
class ItemsControllerTwo(MethodView):

  @blp.response(200, ItemSchema(many=True))
  def get(self):
    return ItemModel.query.all()

  @blp.arguments(ItemSchema)
  @blp.response(201, ItemSchema)
  def post(self, item_data):
    item = None
    try:
      item = ItemModel(**item_data)
      db.session.add(item)
      db.session.commit()
    except SQLAlchemyError as e:
      abort(500, message="Error occoured while insert item data")
    except Exception as e:
      print(e)
    return item
