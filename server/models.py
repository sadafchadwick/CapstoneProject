from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from config import db, bcrypt
# from sqlalchemy import collate



class User( db.Model, SerializerMixin ):
    __tablename__ = 'users'

    id = db.Column( db.Integer, primary_key = True )
    name = db.Column( db.String )
    username = db.Column(db.String)
    password_hash = db.Column( db.String )

# , collate='NOCASE', unique=True

    userfoods = db.relationship('UserFood', back_populates='user')
    foods = association_proxy('userfoods', 'food')

    serialize_rules = ('-userfoods.user', '-foods.users',)


class Food (db.Model, SerializerMixin):
    __tablename__ = 'foods'

    id = db.Column (db.Integer, primary_key=True)
    name = db.Column(db.String)
    amount = db.Column(db.Integer)


    userfoods = db.relationship('UserFood', back_populates='food')
    users = association_proxy ('userfoods', 'user')

    serialize_rules = ('-userfoods.food', '-users.foods',)


class UserFood (db.Model, SerializerMixin):
    __tablename__ = 'userfoods'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    food_id = db.Column(db.Integer, db.ForeignKey('foods.id'))

    user = db.relationship('User', back_populates='userfoods')
    food = db.relationship ('Food', back_populates='userfoods')

    serialize_rules = ('-user.userfoods', '-food.userfoods',)