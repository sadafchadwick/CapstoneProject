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
    
    itemcrate = db.relationship('ItemCrate', back_populates='user', uselist=False, cascade='all,delete-orphan')

    serialize_rules = ('-_password_hash',)
    
    @validates('username')
    def validate_username(self, key, new_username):
        if type(new_username) is str and 3 <= len(new_username):
            return new_username
        raise ValueError('Username must be 5 characters or longer.')
    
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

#each instance of an item (list of items)
class Item (db.Model, SerializerMixin):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    image_url=db.Column(db.String, nullable=True)
    category = db.Column(db.String, nullable=False)
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id')) #who dunit('added by' on the front end)
    
    itemcrates = db.relationship('ItemCrate', back_populates='item')
    
    serialize_rules = ('-itemcrates',)

#list of amounts of each item for each user
class ItemCrate (db.Model, SerializerMixin):
    __tablename__ = 'itemcrates'

    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False, default=0)
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'), nullable=False)
    
    user = db.relationship('User', back_populates='itemcrate')
    item = db.relationship('Item', back_populates='itemcrates')
    
    serialize_rules = ('-item.itemcrates', '-user.itemcrate')