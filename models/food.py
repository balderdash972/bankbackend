# -*- coding: utf-8 -*-]
from db import db


class FoodModel(db.Model):
    __tablename__ = 'foods'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500))
    money = db.Column(db.String(500))

    def __init__(self, name, money):
        self.name = name
        self.money = money

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "money": self.money,
        }

    def saveToDb(self):
        db.session.add(self)
        db.session.commit()

    def deleteFromDb(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def findById(cls, id):
        return cls.query.filter_by(id=id).first()
