# !/usr/bin/env python
# title           :hasher.py
# description     :Enter Description Here
# author          :Sebastian Maldonado
# date            :8/16/2020
# version         :0.0
# usage           :SEE README.md
# notes           :Enter Notes Here
# python_version  :3.6.8
# conda_version   :4.8.3
# =================================================================================================================

import os
import hashlib
from mongoengine import *

BYTE_SIZE = 32


def hash_password(password):

    salt = os.urandom(BYTE_SIZE)

    key = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        salt,
        100000

    )

    return salt + key


def get_salt(hashed_password):

    return hashed_password[:BYTE_SIZE]


def get_key(hashed_password):

    return hashed_password[BYTE_SIZE:]


def verify_password(salt, key, password_to_check):

    new_key = hashlib.pbkdf2_hmac(
        'sha256',
        password_to_check.encode('utf-8'),
        salt,
        100000
    )

    return 1 if new_key == key else 0

