# -*- coding: utf-8 -*-

from pyramid.httpexceptions import HTTPFound
from pyramid.security import remember, forget
from pyramid.view import view_config

from pylonsprojectjp.models import DBSession
from .api import get_user_by_name, verify_password
from .models import UserModel


@view_config(route_name='auth', match_param="action=in", renderer="string",
             request_method="POST")
@view_config(route_name='auth', match_param="action=out", renderer="string")
def sign_in_out(request):
    username = request.POST.get('username')
    if username:
        user = get_user_by_name(username)
        if user and verify_password(user, request.POST.get('password')):
            headers = remember(request, user.name)
        else:
            headers = forget(request)
    else:
        headers = forget(request)
    return HTTPFound(location=request.route_url('home'),
                     headers=headers)
