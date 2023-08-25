from models import User, Food, UserFood
from flask import Flask, request, make_response
from werkzeug.security import generate_password_hash, check_password_hash
from flask_migrate import Migrate
from flask_restful import Api, Resource
import random
import os

from config import app, api, db

@app.route('/')
def index():
    return '<h1>Apocalypse</h1>'

class Login(Resource):
    def post(self):
        data = request.get_json()
        user = User.query.filter(User.user_name == data['userName']).first()
        if not user:
            return make_response({'error': 'Username not found!'}, 404)
        else:
            if user.authenticate(data['password']):
                return make_response(user.to_dict(), 200)
            else:
                return make_response({'error': 'Password does not match!'}, 404)

api.add_resource(Login, '/login')

class Users(Resource):
    def get(self):
        users = User.query.all()
        serialized_users = [user.to_dict(rules=('-rides','-_password_hash')) for user in users]
        return make_response(serialized_users, 200)

    def post(self):
        data = request.get_json()
        try:
            new_user = User(user_name = data['userName'], password_hash = data['password'], name = data['name'])
        except Exception as e:
            return make_response({'error': str(e)}, 404)
        db.session.add(new_user)
        db.session.commit()
        return make_response(new_user.to_dict(), 200)
        # return make_response(new_user.to_dict(only = ('id', 'user_name')), 200)
    
api.add_resource(Users, '/users')

class UserById(Resource):
    def get(self, id):
        user = User.query.filter_by(id=id).first()
        if not user:
            return make_response({'error':'User does not exist'}, 404)
        return make_response(user.to_dict())
    
    def delete(self, id):
        try:
            user = User.query.filter_by(id = id).first()
        except:
            return make_response({"error": "User does not exist"}, 404)

        db.session.delete(user)
        db.session.commit()
        return make_response({}, 204)
    
api.add_resource(UserById, '/users/<int:id>')

class Foods(Resource):
    def get(self):
        foods = Food.query.all()
        return make_response([food.to_dict(only =('id', 'name', 'amount',)) for food in foods], 200)

api.add_resource(Foods, '/foods')

class FoodsById(Resource):
    def get(self, id):
        food = Food.query.filter_by(id=id).first()
        if not food:
            return make_response({"error":"That food does not exist you banana shaped fork!"},404)
        return make_response(food.to_dict())

    def patch(self, id):
        try:
            food = Food.query.filter_by(id = id).first()
            data = request.get_json()
            for attr in data:
                setattr(food, attr, data[attr])
            db.session.commit()
            return make_response(food.to_dict(), 202)
        except AttributeError:
            return make_response({"error": "Food was never entered!"}, 404)
        except ValueError:
            return make_response({"errors": ["validation errors"]}, 400)

    def delete(self, id):
        try:
            user = Food.query.filter_by(id = id).first()
        except:
            return make_response({"error": "This food was never entered!"}, 404)

        db.session.delete(food)
        db.session.commit()
        return make_response({}, 204)

api.add_resource(FoodsById, '/foods/<int:id>')

class UserFoods(Resource):
    def get(self):
        userfoods = UserFood.query.all()
        return make_response([userfood.to_dict() for userfood in userfoods], 200)

api.add_resource(UserFoods, '/userfoods')

if __name__ == '__main__':
    # from models import User, Food, UserFood
    app.run(port=5555, debug=True )






# class Users(Resource):
#     def get(self):
#         users = User.query.all()
#         return make_response([user.to_dict() for user in users], 200)

# api.add_resource(Users, '/users')


# class Signup(Resource):
#     def post(self):
#         username = request.json.get('username')
#         password = request.json.get('password')

#         if not username or not password:
#             return {'message': 'Username and password are required'}, 400

#         existing_user = User.query.filter_by(username=username).first()
#         if existing_user:
#             return {'message': 'Username already taken'}, 409

#         new_user = User(username=username) 
#         new_user.set_password(password)
#         db.session.add(new_user)
#         db.session.commit()

#         return {'message': 'User registered successfully'}, 201

# api.add_resource(Signup, '/signup')



# class UsersById(Resource):
#     def get(self, id):
#         user = User.query.filter_by(id=id).first()
#         if not user:
#             return make_response({"error":"That username does not exist you banana shaped fork!"},404)
#         return make_response(user.to_dict())

#     def patch(self, id):
#         try:
#             user = User.query.filter_by(id = id).first()
#             data = request.get_json()
#             for attr in data:
#                 setattr(user, attr, data[attr])
#             db.session.commit()
#             return make_response(user.to_dict(), 202)
#         except AttributeError:
#             return make_response({"error": "Username was never created!"}, 404)
#         except ValueError:
#             return make_response({"errors": ["validation errors"]}, 400)

#     def delete(self, id):
#         try:
#             user = User.query.filter_by(id = id).first()
#         except:
#             return make_response({"error": "This user was never created!"}, 404)

#         db.session.delete(user)
#         db.session.commit()
#         return make_response({}, 204)

# api.add_resource(UsersById, '/users/<int:id>')