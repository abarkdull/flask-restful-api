import os

from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_jwt import JWT


# grabs working directory
basedir = os.path.abspath(os.path.dirname(__file__))

# initalize and configure app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL_CUSTOM")
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# set instance of db and api with app
db = SQLAlchemy(app)
api = Api(app)


# before first request, create database
@app.before_first_request
def create_tables():
    db.create_all()

@app.route("/")
def index():
    return {
        "message": "welcome to my API"
    }


from rest_api.security import authenticate, identity 

jwt = JWT(app, authenticate, identity)
app.config["JWT_SECRET_KEY"] = os.environ.get("JWT_SECRET_KEY")
app.config["JWT_ALGORITHM"] = os.environ.get("JWT_ALGORITHM")
app.config["JWT_AUTH_ENDPOINT"] = os.environ.get("JWT_AUTH_ENDPOINT")


from resources.item import ItemList, ItemResource
from resources.register import Register

api.add_resource(ItemList, "/items")
api.add_resource(ItemResource, "/item/<name>")
api.add_resource(Register, '/register')