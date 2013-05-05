# -*- coding: utf-8 -*-

from .models import UserModel


def get_user_by_name(name):
    return UserModel.query().filter(UserModel.name == name).first()


def verify_password(user, password):
    return user.password == password
