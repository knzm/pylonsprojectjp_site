# -*- coding: utf-8 -*-

from pyramid.view import view_config


@view_config(route_name='home', renderer="pylonsprojectjp:templates/index.jinja2")
def index(request):
    return {}
