from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from config import db, bcrypt
# from sqlalchemy import collate

class User( db.Model, SerializerMixin ):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    username = db.Column(db.String)
    _password_hash = db.Column(db.String, nullable = False)

    inventories = db.relationship('Inventory', back_populates='user')
    items = association_proxy('inventories', 'item')

    serialize_rules = ('-inventories.user', '-items.users',)

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

class Category (db.Model, SerializerMixin):
    __tablename__ = 'categories'

    id = db.Column (db.Integer, primary_key=True)
    name = db.Column(db.String)

    items = db.relationship('Item', back_populates='category')

    serialize_rules = ('-items.category',)

#which user has which items:(post, delete, edit, get)
class Inventory (db.Model, SerializerMixin):
    __tablename__ = 'inventories'

    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'))

    user = db.relationship('User', back_populates='inventories')
    item = db.relationship ('Item', back_populates = 'inventories')
    
    serialize_rules = ('-user.inventories','-items.inventories',)

class Item (db.Model, SerializerMixin):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))

    category = db.relationship ('Category', back_populates='items')
    inventories = db.relationship('Inventory', back_populates='item')
    
    serialize_rules = ('-inventories.item','-category.items',)