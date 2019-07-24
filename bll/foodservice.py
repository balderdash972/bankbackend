# -*- coding: utf-8 -*-]
from models.food import FoodModel


class FoodService():
    def __init__(self):
        pass

    def Food(self, id):
        res = []
        food = FoodModel.findById(id)
        if food is None:
            return {'message': 'Food not found.'}, 404
        temp_food = food.to_dict()
        if temp_food:
            return temp_food
            res.append(temp_food)
        return {"result": res}

    def Foods(self):
        #res = []

        query_all_fm = FoodModel.query.all()
        res = [f.to_dict() for f in query_all_fm]
        #totol_num = 0
        #totol_num_neg = 0
        # for f in query_all_fm:
        #    temp_json = f.to_dict()
        #    res.append(temp_json)
        # print(temp_json)
        #totol_num += int(temp_json["money"])
        #totol_num_neg += int(temp_json["money"]) if int(temp_json["money"])<0 else 0
        # for b in res:
        #    a = int(b["money"])
        #a += a
        #    print(a)

        total = {
            "balance": sum([int(x["money"]) for x in res]),  # totol_num,
            # totol_num_neg
            "cost": sum([int(x["money"]) if int(x["money"]) < 0 else 0 for x in res])
        }
        return {
            "balance": sum([int(x["money"]) for x in res]),
            "cost": sum([int(x["money"]) if int(x["money"]) < 0 else 0 for x in res]),
            "result": res
        }
