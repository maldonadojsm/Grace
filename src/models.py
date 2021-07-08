# !/usr/bin/env python
# title           :models.py
# description     :Database's Schemas
# author          :Sebastian Maldonado
# date            :8/15/2020
# version         :0.0
# usage           :SEE README.md
# notes           :Enter Notes Here
# python_version  :3.6.8
# conda_version   :4.8.3
# =================================================================================================================


from mongoengine import *
from datetime import *
import json
from bson import json_util


class Patient(Document):

    patient_id = StringField(required=True, unique=True)
    username = StringField(required=True, unique=True)
    name = ListField(StringField(required=True))
    password = BinaryField(required=True)
    email = EmailField(required=True, unique=True)
    age = IntField(required=True)
    gender = StringField(required=True, max_length=1)
    birth_date = StringField(required=True)

    def json(self):
        patient_dict = {
            "patient_id": self.patient_id,
            "username": self.username,
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
            "birth_date": self.birth_date,
            "email": self.email,
            "password": self.password
        }

        return json.dumps(patient_dict)

    meta = {
        "indexes": ["username", "email"],
        "ordering": ["-birth_date"]
    }


class Result(Document):

    result_id = StringField(required=True, unique=True)
    patient_id = StringField()
    results = ImageField()

    def json(self):
        result_dict = {
            "result_id": self.result_id,
            "patient_id": self.patient_id,
            "results": self.results
        }

        return json.dumps(result_dict, default=json_util.default)

    meta = {
        "indexes": ["result_id"],
        "ordering": ["-result_id"]
    }


class Order(Document):

    order_id = StringField(required=True, unique=True)
    patient_id = StringField(required=True)
    sample_id = StringField(required=True, unique=True)
    sample_list = ListField(StringField(required=True))
    order_date = DateTimeField(default=datetime.now())
    status = StringField(required=True, default="Order Placed")

    def json(self):
        order_dict = {
            "order_id": self.order_id,
            "patient_id": self.patient_id,
            "sample_id": self.sample_id,
            "sample_list": self.sample_list,
            "order_date": self.order_date,
            "status": self.status
        }

        return json.dumps(order_dict, default=json_util.default)

    meta = {
        "indexes": ["order_id"],
    }
