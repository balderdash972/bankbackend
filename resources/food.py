# -*- coding: utf-8 -*-
import sqlite3
from flask_restful import Resource, reqparse
from models.food import FoodModel
from bll.foodservice import FoodService


class Foods(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name')
    parser.add_argument('money')

    def post(self):
        data = Foods.parser.parse_args()
        food = FoodModel(**data)
        try:
            food.saveToDb()
        except:
            return {"message": "An error occurred while creating the classroom."}, 500
        return food.to_dict(), 201


    def get(self):
        foods = FoodService()
        return foods.Foods()


class Food(Resource):
    def get(self, id):
        food = FoodService()
        return food.Food(id)

    def put(self, id):
        data = Foods.parser.parse_args()
        food = FoodModel.findById(id)

        if food is None:
            return {'message': 'Food not found.'}
        else:
            food.name = data['name']
            food.money = data['money']
        food.saveToDb()
        return food.to_dict()

    def delete(self, id):
        food = FoodModel.findById(id)
        if food:
            food.deleteFromDb()
            return {'message': 'Food deleted.'}
        return {'message': 'Food not found.'}, 404


