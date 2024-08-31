from flask import Flask, request

app = Flask(__name__)

stores = [
  {
    "name":"My Store",
    "items" : [
      {
        "name":"Chair",
        "price":15.77
      },
      {
        "name":"Bucket",
        "price": 8.50
      }
    ]
  }
]


@app.get("/store")
def get_stores():
  return {"stores": stores}

@app.post("/store")
def create_store():
  request_json = request.get_json()
  new_store = {"name" : request_json["name"], "items":[]}
  stores.append(new_store)
  return new_store, 201

@app.post("/store/<string:name>/item")
def create_item(name):
  request_data = request.get_json()
  for store in stores:
    if store["name"] == name:
      new_item = {"name":request_data["name"], "price":request_data["price"]}
      store["items"].append(new_item)
      return new_item, 201
  return {"message":"Store not found"}, 404


@app.get("/store/<string:name>")
def get_store(name):
  for store in stores:
    if store["name"] == name:
      return store, 200
  return {"message":"Store not found"}, 404

@app.get("/store/<string:name>/item")
def get_item(name):
  for store in stores:
    if store["name"] == name:
      return {"items": store["items"], "message":"You are rock"}, 200
  return {"message":"Store not found"}, 404

