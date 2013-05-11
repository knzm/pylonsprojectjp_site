# -*- coding: utf-8 -*-

from pkg_resources import resource_filename

from pyramid.view import view_config, notfound_view_config
from pyramid.asset import resolve_asset_spec
from pyramid.response import FileResponse


@notfound_view_config()
def notfound_view(request):
    package, filename = resolve_asset_spec('pylonsprojectjp:static/404.html',
                                           request.registry.__name__)
    path = resource_filename(package, filename)
    return FileResponse(path)


@view_config(route_name='home', renderer="pylonsprojectjp:templates/index.jinja2")
def index(request):
    return {}
