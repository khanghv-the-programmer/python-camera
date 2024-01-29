from flask import Flask,jsonify,request,Blueprint
from Services.API.Users.EditUser import ns as EditUser
from flask_restplus import Api
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
db = SQLAlchemy()

def configure_app(flask_app):
    flask_app.config['ENVIRONMENT_VARIABLE'] = 1
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = 'list'
    flask_app.config['RESTPLUS_VALIDATE'] = True
    flask_app.config['RESTPLUS_MASK_SWAGGER'] = False
    flask_app.config['ERROR_404_HELP'] = False
    flask_app.config['ORM_SCHEMAS'] = ["AKABI_DWH_URI"]
    flask_app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
        "pool_pre_ping": True,
        "pool_recycle": 300,
    }

def initialize(flask_app):
    Camera = Blueprint('api', __name__, url_prefix='/api')
    api = Api(app)
    api.init_app(Camera)
    api.add_namespace(EditUser)
    flask_app.register_blueprint(Camera)
    db.init_app(flask_app)


def main():
    configure_app(app)
    initialize(app)
    app.run(debug=True, host="0.0.0.0", port=8080)


if __name__ == "__main__":
    main()
