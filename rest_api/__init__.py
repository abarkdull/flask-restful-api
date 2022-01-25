from flask import Flask
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
import os

from flask_jwt import JWT


# grabs working directory
basedir = os.path.abspath(os.path.dirname(__file__))


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SECRET_KEY'] = 'austin'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
api = Api(app)

from rest_api.security import authenticate, identity 

jwt = JWT(app, authenticate, identity)


from resources.item import ItemList, ItemResource
from resources.register import Register

api.add_resource(ItemList, "/items")
api.add_resource(ItemResource, "/item/<name>")
api.add_resource(Register, '/register')