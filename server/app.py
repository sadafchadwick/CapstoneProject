from models import User, Food, UserFood
from flask import Flask, request, make_response, session
# from flask_migrate import Migrate
from flask_restful import Resource
from config import app, api, db, CORS, migrate



@app.route('/')
def index():
    return '<h1>Apocalypse</h1>'

class Login(Resource):
    def post(self):
        data = request.get_json()
        user = User.query.filter(User.username == data['username']).first()
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
            new_user = User(name = data['name'], username = data['username'], password_hash = data['password'] )
        except Exception as e:
            return make_response({'error': str(e)}, 404)
        db.session.add(new_user)
        db.session.commit()
        return make_response(new_user.to_dict(), 200)
    
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
    app.run(port=5555, debug=True )