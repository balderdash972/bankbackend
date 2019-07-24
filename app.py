# -*- coding: utf-8 -*-
from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from resources.food import Foods, Food

app = Flask(__name__)
CORS(app)


# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://Dex3084:Dex3084@192.168.3.245/lungteng?charset=utf8'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_POOL_RECYCLE'] = 60
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
# app.secret_key = 'jose'
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(Foods, '/bank/api/foods')
api.add_resource(Food, '/bank/api/food/<int:id>')


@app.route("/")
def home():
    return "Hello World"


if __name__ == "__main__":
    from db import db
    db.init_app(app)
    app.run(debug=True)
