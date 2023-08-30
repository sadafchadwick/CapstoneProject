from models import User, Item, ItemCrate
from flask import Flask, request, make_response, session, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, reqparse, abort
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
        try:
            new_user = User(name = data['name'], username = data['username'], password_hash = data['password'] )
        except ValueError as v:
            return make_response({'error': str(v)}, 404)
        db.session.add(new_user)
        db.session.commit()
        # allows to login user after successful signup
        session['user_id']=new_user.id
        return make_response(new_user.to_dict(), 201)
    
api.add_resource(Signup, '/signups')

class Users(Resource):
    def get(self):
        users = User.query.all()
        users_data = [{'id':user.id, 'name':user.name, 'username':user.username} for user in users]
        return make_response(users_data, 200) 

api.add_resource(Users, '/users')

class UserById(Resource):
    def get(self, id):
        user = User.query.filter_by(id=id).first()
        if not user:
            return make_response({'error':'User does not exist'}, 404)
        return make_response(user.to_dict())

    def patch(self, id):
        user = User.query.get_or_404(id)
        data = request.get_json()
        for attr in data:
            setattr(user, attr, data[attr])
        db.session.commit()
        return make_response (user.to_dict(), 202)

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

class Items(Resource):
    def get(self):
        items = Item.query.all()
        return make_response([item.to_dict() for item in items], 200)
    
    def post(self):
        data = request.get_json()
        try:
            new_item = Item(name = data['name'], image_url = data['image_url'], category = data['category'] )
        except Exception as e:
            return make_response({'error': str(e)}, 404)
        db.session.add(new_item)
        db.session.commit()
        return make_response(new_item.to_dict(), 201)

api.add_resource(Items, '/items')

class ItemCrates(Resource):
    def get(self):
        itemcrates = ItemCrate.query.all()
        return make_response([itemcrate.to_dict() for itemcrate in itemcrates], 200)
    
    def post(self):
        data = request.get_json()
        try:
            new_itemcrate = ItemCrate(
                quantity = data['quantity'],
                item_id = data['item_id'],
                user_id = data['user_id']
                )
            
        except Exception as e:
            return make_response({'error': str(e)}, 404)
        db.session.add(new_itemcrate)
        db.session.commit()
        return make_response(new_itemcrate.to_dict(), 201)

api.add_resource(ItemCrates, '/itemcrates')

class ItemCrateByUserId(Resource):
    def get(self, user_id=None):
        if user_id is None:
            itemcrates = ItemCrate.query.all()
        else:
            itemcrates = ItemCrate.query.filter_by(user_id=user_id).all() 
        itemcrates_data = [itemcrate.to_dict() for itemcrate in itemcrates]
        return make_response(itemcrates_data)
    
    def delete(self, user_id):
        try:
            itemcrate = ItemCrate.query.filter_by(id = user_id).first()
        except:
            return make_response({"error": "This item was not deleted!"}, 404)
        db.session.delete(itemcrate)
        db.session.commit()
        return make_response({}, 204)

api.add_resource(ItemCrateByUserId, '/itemcrates/<int:user_id>')




if __name__ == '__main__':
    app.run(port=5555, debug=True )
    
    
#     def post(self, user_id):
#         args = parser_inventory.parse_args()
#         item_id = args['item_id']
#         quantity = args['quantity']

#         user = User.query.get(user_id)
#         item = Item.query.get(item_id)

#         if not user or not item:
#             abort(404, message="User or Item not found")

#         inventory_entry = Inventory.query.filter_by(user=user, item=item).first()

#         if inventory_entry:
#             inventory_entry.quantity += quantity
#         else:
#             inventory_entry = Inventory(user=user, item=item, quantity=quantity)
#             db.session.add(inventory_entry)
        
#         db.session.commit()
#         return inventory_entry.serialize()

#     def delete(self, user_id, inventory_id):
#         inventory_entry = Inventory.query.get(inventory_id)
#         if inventory_entry and inventory_entry.user_id == user_id:
#             db.session.delete(inventory_entry)
#             db.session.commit()
#             return '', 204  # No content
#         else:
#             abort(404, message="Inventory entry not found or does not belong to the user")
    
# # class Inventories(Resource):
# #     def get(self):
# #         inventories = Inventory.query.all()
# #         return make_response([inventory.to_dict() for inventory in inventories], 200)

# # api.add_resource(Inventories, '/inventories')

# # class InventoriesById(Resource):
# #     def get(self, id):
# #         inventory = Inventory.query.filter_by(id=id).first()
# #         if not inventory:
# #             return make_response({"error":"That inventory item does not exist!"},404)
# #         return make_response(inventory.to_dict())
    


# #     def patch(self, id):
# #         try:
# #             inventory = Inventory.query.first()
# #             data = request.get_json()
# #             for attr in data:
# #                 setattr(inventory, attr, data[attr])
# #             db.session.commit()
# #             return make_response(inventory.to_dict(), 202)
# #         except AttributeError:
# #             return make_response({"error": "inventory was never entered!"}, 404)
# #         except ValueError:
# #             return make_response({"errors": ["validation errors"]}, 400)

# #     def delete(self, id):
# #         try:
# #             inventory = Inventory.query.filter_by(id = id).first()
# #         except:
# #             return make_response({"error": "This inventory was never entered!"}, 404)

# #         db.session.delete(inventory)
# #         db.session.commit()
# #         return make_response({}, 204)

# # api.add_resource(InventoriesById, '/inventories/<int:user_id>')