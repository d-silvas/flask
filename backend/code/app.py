from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from db import db
from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../data.db'
# Turns off the flask sqlalchemy modification tracker, does not turn off
# the sqlalchemy one (see docs)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True  # To see flask_jwt errors
# This has to actually be secret (read documentation)
app.secret_key = 'qqq'
api = Api(app)


@app.before_first_request
def create_database():
    db.create_all()


# Creates new endpoint /auth
jwt = JWT(app, authenticate, identity)

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')

# See video 85 for explanation about imports
if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)
