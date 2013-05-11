# -*- coding: utf-8 -*-

from pyramid_layout.panel import panel_config

from .api import get_login_form_value


@panel_config('login_form', renderer='pylonsprojectjp:templates/auth/panels/login_form.mako')
def login_form(context, request, form_value, form_error):
    form_value = get_login_form_value(request)

    return {
        "location": form_value['location'],
        "username": form_value['username'],
        # For security reason, we refuse to use the password
        # passed via GET parameter.
        "password": "",
        "login_url": request.route_url("login"),
        }
