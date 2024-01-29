from flask import Flask,jsonify,request,Blueprint
from flask_swagger_ui import get_swaggerui_blueprint
from Services.API.Users.EditUser import CreateUser
from flask_restplus import Api
import json

app = Flask(__name__)

SWAGGER_URL = "/Camera"
API_URL = "/static/swagger.json"

swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': 'Camera API'
    }
)
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)


@app.route("/")
def home():
    return jsonify({
        "Message": "app up and running successfully"
    })

@app.route("/users/access",methods=["POST"])
def access():
    data = request.get_json()
    name = data.get("name", "dipto")
    server = data.get("server","server1")

    message = f"User {name} received access to server {server}"

    return jsonify({
        "Message": message
    })


if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0",port=8080)

