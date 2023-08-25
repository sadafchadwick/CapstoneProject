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
    _password_hash = db.Column(db.String, nullable = False)

# , collate='NOCASE', unique=True

    userfoods = db.relationship('UserFood', back_populates='user')
    foods = association_proxy('userfoods', 'food')

    serialize_rules = ('-userfoods.user', '-foods.users',)

    @property
    def password_hash(self):
        return self._password_hash
    
    @password_hash.setter
    def password_hash(self, new_password):
        enc_new_password = new_password.encode('utf-8')
        encrypted_hash = bcrypt.generate_password_hash(enc_new_password)
        hash_password_str = encrypted_hash.decode('utf-8')
        self._password_hash = hash_password_str

    def authenticate(self, password):
        enc_password = password.encode('utf-8')
        return bcrypt.check_password_hash(self._password_hash, enc_password)


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

# from flask_sqlalchemy import SQLAlchemy
# from werkzeug.security import generate_password_hash, check_password_hash

# db = SQLAlchemy()

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(50), unique=True, nullable=False)
#     password_hash = db.Column(db.String(128), nullable=False)

#     # Define relationships
#     foods = db.relationship('Food', backref='user', lazy=True)
#     weapons = db.relationship('Weapon', backref='user', lazy=True)
#     medical_supplies = db.relationship('MedicalSupply', backref='user', lazy=True)
#     survival_gear = db.relationship('SurvivalGear', backref='user', lazy=True)

#     def set_password(self, password):
#         self.password_hash = generate_password_hash(password)

#     def check_password(self, password):
#         return check_password_hash(self.password_hash, password)

# class Food(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     amount = db.Column(db.Integer, nullable=False)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# class Weapon(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     quantity = db.Column(db.Integer, nullable=False)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# class MedicalSupply(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     count = db.Column(db.Integer, nullable=False)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# class SurvivalGear(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     quantity = db.Column(db.Integer, nullable=False)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)