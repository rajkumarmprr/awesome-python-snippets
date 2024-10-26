from flask import Flask
from flask_smorest import Api
from resources.stores import blp as StoresModule
from resources.items import blp as ItemsModule

app = Flask(__name__)

app.config["PROPOGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "Store REST API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/apidoc"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)

api.register_blueprint(StoresModule)
api.register_blueprint(ItemsModule)