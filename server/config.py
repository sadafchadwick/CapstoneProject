# Standard library imports

# Remote library imports
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from flask_bcrypt import Bcrypt

# Local imports

# Instantiate app, set attributes
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

# Define metadata, instantiate db
metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})
db = SQLAlchemy(metadata=metadata)
migrate = Migrate(app, db)
db.init_app(app)

# Instantiate REST API
api = Api(app)
bcrypt = Bcrypt(app)

# Instantiate CORS
CORS(app, origins=["http://localhost:3000"])


#this is creating a secret key for session to be used:
def get_secret_key_from_file(file_path):
    with open (file_path, 'rb') as f:
        secret_key = f.read().strip()
    return secret_key

app.secret_key = get_secret_key_from_file('secretkey.env')

# app.secret_key = b'B/\xf4\rGD\xd8)\x90!\x123A\x85\x13\xfc'