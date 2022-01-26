from rest_api import db


class Item(db.Model):

    __tablename__ = "Items"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def json(self):
        return {'name': self.name,
                'price': self.price}


    @classmethod
    def get_all_items(cls):

        return { "items": [ item.json() for item in Item.query.all() ]}


class User(db.Model):

    __tablename__ = "Users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password


# To create tables from scratch, uncomment below line, 
# open python interactive shell and type:
# "from rest_api import models"
# 
# db.create_all()
