# -*- coding: utf-8 -*-

from pyramid.httpexceptions import HTTPNotFound
from pyramid.view import view_config

from .api import get_page


@view_config(route_name="page", renderer="pylonsprojectjp:templates/page/index.jinja2")
def page_view(request):
    subpath = request.matchdict["subpath"]
    page = get_page(subpath)
    if page is None:
        raise HTTPNotFound
    return {
        "title": page.title,
        "body": page.body,
        }
