# -*- coding: utf-8 -*-

from pyramid.security import remember, forget, authenticated_userid
from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config, forbidden_view_config

from .api import get_login_form_value
from .security import authenticate


@forbidden_view_config(
    layout="auth", renderer='pylonsprojectjp:templates/auth/login.mako')
@view_config(route_name="login", request_method='GET', layout="auth",
             renderer='pylonsprojectjp:templates/auth/login.mako')
def login_form(context, request):
    if authenticated_userid(request):
        location = request.route_url('admin_redirect')
        return HTTPFound(location=location)

    return {
        "message": "",
        }


@view_config(route_name="login", request_method='POST', layout="auth",
             renderer='pylonsprojectjp:templates/auth/login.mako')
def login(context, request):
    if authenticated_userid(request):
        location = request.route_url('admin_redirect')
        return HTTPFound(location=location)

    form_value = get_login_form_value(request)
    location = form_value['location']
    username = form_value['username']
    password = form_value['password']

    user = authenticate(request, username, password)
    if user:
        headers = remember(request, username)
        return HTTPFound(location=location, headers=headers)

    return {
        "location": location,
        "username": username,
        "password": password,
        "message": "Login Failed",
        }


@view_config(route_name="logout")
def logout(context, request):
    headers = forget(request)
    location = request.route_url('login')
    return HTTPFound(location=location, headers=headers)
