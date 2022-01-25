from flask_restful import Resource, reqparse
from rest_api.models import Item
from rest_api import db
from flask_jwt import jwt_required


# get all items
class ItemList(Resource):

    @jwt_required()
    def get(self):
        items = Item.query.all()
        items_json = []

        for item in items:
            new_item = {
                "name": item.name,
                "price": item.price
            }
            items_json.append(new_item)

        if items:
            return items_json
        else:
            return None


class ItemResource(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help="This field cannot be left blank")

    def get(self, name):

        item = Item.query.filter_by(name=name).first()
        if item:
            return {"name": item.name,
                    "price": item.price}, 202
        else:
            return {"message": "item not found"}
    
    def post(self, name):
        
        # if item already exists return a message
        if Item.query.filter_by(name=name).first():
            return {"message": f"An item with name {name} already exists."}
        
        data = ItemResource.parser.parse_args()
        new_item = Item(name=name, price=data['price'])

        db.session.add(new_item)
        db.session.commit()

        
        return {"message": f"item {name} inserted succesfully."}

    def delete(self, name):

        item_to_delete = Item.query.filter_by(name=name).first()

        if item_to_delete:
            db.session.delete(Item.query.filter_by(name=name).first())
            db.session.commit()
            return {"message": f"item {name} succesfully deleted."}

        else:
            return {"message": f"item {name} could not be found"}