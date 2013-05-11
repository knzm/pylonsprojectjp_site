# -*- coding: utf-8 -*-

from pyramid.httpexceptions import HTTPNotFound, HTTPFound
from pyramid.view import view_config

from pylonsprojectjp.models import DBSession

from .api import get_paginator
from .models import BlogEntryModel


@view_config(route_name='blog_index', renderer="pylonsprojectjp:templates/blog/index.jinja2")
def blog_index_view(request):
    page = int(request.params.get('page', 1))
    paginator = get_paginator(request, page)
    return {'paginator': paginator}


@view_config(route_name='blog_entry', renderer="pylonsprojectjp:templates/blog/view.jinja2")
def blog_entry_view(request):
    id = int(request.matchdict.get('id', -1))
    entry = BlogEntryModel.get_by_id(id)
    if not entry:
        return HTTPNotFound()
    return {'entry': entry}
