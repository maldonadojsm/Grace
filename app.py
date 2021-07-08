# !/usr/bin/env python
# title           :app.py
# description     :Flask App
# author          :Sebastian Maldonado
# date            :8/16/2020
# version         :0.0
# usage           :SEE README.md
# notes           :Enter Notes Here
# python_version  :3.6.8
# conda_version   :4.8.3
# =================================================================================================================


from flask import Flask, request
from src.services import *
from src.hasher import *

DB_URI = "mongodb+srv://grace:grace12345@cluster0.fqvje.mongodb.net/grace?retryWrites=true&w=majority"

connect(host=DB_URI)


app = Flask(__name__)

# Prompt 4
@app.route("/api/order", methods=["POST"])
def create_order():
    request_payload = request.json
    order = request_payload["order"]

    # Validate User
    try:
        user = Patient.objects(username=order["username"]).get()
    except DoesNotExist:
        return "Username Not Found"

    # Verify Password

    salt = get_salt(user.password)
    key = get_key(user.password)

    # Process Order
    if verify_password(salt, key, order["password"]):
        generate_order(user, order["samples"])
        return "Order Successfully Created"
    else:
        return "Password Incorrect"


@app.route("/api/order", methods=["GET"])
def get_orders():

    request_payload = request.json
    order = request_payload["order"]

    # Validate User
    try:
        user = Patient.objects(username=order["username"]).get()
    except DoesNotExist:
        return "Username Not Found"

    # Verify Password

    salt = get_salt(user.password)
    key = get_key(user.password)

    # Process Order
    if verify_password(salt, key, order["password"]):
        patient_orders = retrieve_order(user)
        return patient_orders
    else:
        return "Password Incorrect"


@app.route("/api/result", methods=["GET"])
def get_result():

    request_payload = request.json
    result = request_payload["result"]

    # Validate User
    try:
        user = Patient.objects(username=result["username"]).get()
    except DoesNotExist:
        return "Username Not Found"

    # Verify Password

    salt = get_salt(user.password)
    key = get_key(user.password)

    # Process Order
    if verify_password(salt, key, result["password"]):
        patient_result = retrieve_order(result)
        return patient_result
    else:
        return "Password Incorrect"


@app.route("/api/register", methods=["POST"])
def register_user():

    request_payload = request.json
    user = request_payload["user"]

    try:
        register_patient(user)
        return "User Created Successfully"
    except NotUniqueError:
        return "Error: User Already Exists"


if __name__ == "__main__":
    app.run(debug=1)

