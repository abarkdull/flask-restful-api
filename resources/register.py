from flask_restful import Resource, reqparse
from rest_api.models import User
from rest_api import db

class Register(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required=True,
        help="This field cannot be left blank")
    parser.add_argument('password',
        type=str,
        required=True,
        help="This field cannot be left blank")

    
    def get(self):

        users = User.query.all()
        users_lst = []

        for user in users:
            users_lst.append({
                "username": user.username,
                "password": user.password
            })

        return users_lst


    def post(self):

        data = Register.parser.parse_args()
        username = data['username']
        password = data['password']

        if User.query.filter_by(username=username).first():
            return {"message": f"Username {username} already exists"}
        
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()

        return {"message": f"User {username} created succesfully."}

