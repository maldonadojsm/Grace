# !/usr/bin/env python
# title           :services.py
# description     :Enter Description Here
# author          :Sebastian Maldonado
# date            :8/16/2020
# version         :0.0
# usage           :SEE README.md
# notes           :Enter Notes Here
# python_version  :3.6.8
# conda_version   :4.8.3
# =================================================================================================================

from models import *
import uuid
from hasher import *
from datetime import *


def register_patient(payload):

    Patient(
        patient_id=str(uuid.uuid4()),
        username=payload["username"],
        name=payload["name"],
        email=payload["email"],
        gender=payload["gender"],
        birth_date=payload["birth_date"],
        age=payload["age"],
        password=hash_password(payload["password"])

    ).save()


def generate_order(patient, samples):

    Order(
        order_id=str(uuid.uuid4()),
        sample_id=str(uuid.uuid4()),
        patient_id=patient.patient_id,
        sample_list=samples

    ).save()


def store_result(patient, img):

    Result(

        result_id=str(uuid.uuid4()),
        patient_id=patient.patient_id,
        result=img
    ).save()


def retrieve_result(patient):

    try:
        results = Result.objects(patient_id=patient.patient_id).get()

    except DoesNotExist:
        return "No Results Found"

    return results


def retrieve_order(patient):

    try:
        orders = Order.objects(patient_id=patient.patient_id)

    except DoesNotExist:
        return "No Results Found"

    order_dict = dict()

    for i in orders:
        order_dict[i.order_id] = i.json()

    return json.dumps(order_dict)
