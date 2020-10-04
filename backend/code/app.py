from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList

app = Flask(__name__)
# This has to actually be secret (read documentation)
app.secret_key = 'qqq'
api = Api(app)

# Creates new endpoint /auth
jwt = JWT(app, authenticate, identity)

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

# See video 85 for explanation about imports
if __name__ == '__main__':
    app.run(port=5000, debug=True)
