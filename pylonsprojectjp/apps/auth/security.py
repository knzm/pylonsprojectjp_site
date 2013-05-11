# -*- coding: utf-8 -*-

import hashlib

from pyramid.security import authenticated_userid

__all__ = [
    'hash_password',
    'get_user_by_username',
    'get_current_user',
    'authenticate',
]


def hash_password(password, salt=""):
    return hashlib.sha1(salt + password).hexdigest()


def get_user_by_username(username):
    from pylonsprojectjp.models import DBSession
    from .models import UserModel

    query = DBSession.query(UserModel)
    return query.filter_by(username=username).first()


def get_current_user(request):
    username = authenticated_userid(request)
    if username:
        return get_user_by_username(username)
    else:
        return None


def authenticate(request, username, password):
    user = get_user_by_username(username)
    if user is None:
        return False
    return user.verify_password(password)
