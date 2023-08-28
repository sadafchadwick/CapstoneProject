from models import User, Category, Inventory
from flask import Flask, request, make_response, session
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
                session['user_id'] = user.id
                print(session.get('user_id'))
                return make_response(user.to_dict(), 200)
            else:
                return make_response({'error': 'Password does not match!'}, 404)

api.add_resource(Login, '/login')

class Logout(Resource):
    def delete(self):
        session['user_id'] = None
        return make_response({'message':'You have been successfully logged out!'}, 204)
    
api.add_resource(Logout, '/logout')

class CheckSession(Resource):
    def get(self):
        user = User.query.filter(User.id == session.get('user_id')).first()
        if not user:
            return make_response({'error': 'User is not authorized to enter!'}, 401)
        else:
            return make_response(user.to_dict(), 200)
        
api.add_resource(CheckSession, '/check_session')

class Signup(Resource):
    def post(self):
        data = request.get_json()
        # name = data.get('name')
        # username = data.get('username')
        # password_hash = data.get('password')
        try:
            new_user = User(name = data['name'], username = data['username'], password_hash = data['password'] )
        except Exception as e:
            return make_response({'error': str(e)}, 404)
        # if User.query.filter_by(username=username).first():
        #     return {'message': 'Username already exists! Be original for once!'}
        # new_user = User(name=name, username=username, password_hash=password)
        db.session.add(new_user)
        db.session.commit()
        session.get['user_id']=new_user.id
        return make_response(new_user.to_dict(), 201)
    
api.add_resource(Signup, '/signups')

class Users(Resource):
    def get(self):
        users = User.query.all()
        users_data = [{'id':user.id, 'name':user.name, 'username':user.username} for user in users]
        session.get['user_id']=new_user.id
        return make_response(users_data, 200) 

api.add_resource(Users, '/users')


class UserById(Resource):
    def get(self, id):
        user = User.query.filter_by(id=id).first()
        if not user:
            return make_response({'error':'User does not exist'}, 404)
        return make_response(user.to_dict())
    
    def patch(self, id):
        user = User.query.get_or_404(user_id)
        data = request.get_json()
        if 'name' in data:
            user.name = data['name']
        if 'username' in data:
            user.username = data['username']
        if 'password' in data:
            user.password = data['password']
        db.session.commit()
        return {'message': 'User updated successfully'}
    
    def delete(self, id):
        try:
            user = User.query.filter_by(id = id).first()
        except:
            return make_response({"error": "User does not exist"}, 404)

        db.session.delete(user)
        db.session.commit()
        session['user_id'] = None
        return make_response({}, 204)
    
api.add_resource(UserById, '/users/<int:id>')

class Categories(Resource):
    def get(self):
        categories = Category.query.all()
        return make_response([category.to_dict(only =('id', 'name', )) for category in categories], 200)

api.add_resource(Categories, '/categories')

class CategoriesById(Resource):
    def get(self, id):
        category = Category.query.filter_by(id=id).first()
        if not category:
            return make_response({"error":"That category does not exist!"},404)
        return make_response(category.to_dict())

    def patch(self, id):
        try:
            category = Category.query.filter_by(id = id).first()
            data = request.get_json()
            for attr in data:
                setattr(category, attr, data[attr])
            db.session.commit()
            return make_response(category.to_dict(), 202)
        except AttributeError:
            return make_response({"error": "category was never entered!"}, 404)
        except ValueError:
            return make_response({"errors": ["validation errors"]}, 400)

    def delete(self, id):
        try:
            user = Category.query.filter_by(id = id).first()
        except:
            return make_response({"error": "This category was never entered!"}, 404)

        db.session.delete(category)
        db.session.commit()
        return make_response({}, 204)

api.add_resource(CategoriesById, '/categories/<int:id>')

class Inventories(Resource):
    def get(self):
        inventories = Inventory.query.all()
        return make_response([inventory.to_dict() for inventory in inventories], 200)

api.add_resource(Inventories, '/inventories')

if __name__ == '__main__':
    app.run(port=5555, debug=True )