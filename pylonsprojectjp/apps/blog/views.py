# -*- coding: utf-8 -*-

from pyramid.httpexceptions import HTTPNotFound, HTTPFound
from pyramid.view import view_config

from pylonsprojectjp.models import DBSession

from .api import get_paginator
from .models import EntryModel
from .forms import BlogCreateForm, BlogUpdateForm


@view_config(route_name='blog_index', renderer="pylonsprojectjp:templates/blog/index.jinja2")
def blog_index_view(request):
    page = int(request.params.get('page', 1))
    paginator = get_paginator(request, page)
    return {'paginator': paginator}


@view_config(route_name='blog_entry', renderer="pylonsprojectjp:templates/blog/view.jinja2")
def blog_entry_view(request):
    id = int(request.matchdict.get('id', -1))
    entry = EntryModel.by_id(id)
    if not entry:
        return HTTPNotFound()
    return {'entry': entry}


@view_config(route_name='blog_action', match_param="action=create",
             renderer="pylonsprojectjp:templates/blog/edit.jinja2",
             permission='create')
def blog_create_view(request):
    entry = EntryModel()
    form = BlogCreateForm(request.POST)
    if request.method == 'POST' and form.validate():
        form.populate_obj(entry)
        DBSession.add(entry)
        return HTTPFound(location=request.route_url('home'))
    return {'form': form, 'action': request.matchdict.get('action')}


@view_config(route_name='blog_action', match_param="action=edit",
             renderer="pylonsprojectjp:templates/blog/edit.jinja2",
             permission='edit')
def blog_update_view(request):
    id = int(request.params.get('id', -1))
    entry = EntryModel.by_id(id)
    if not entry:
        return HTTPNotFound()
    form = BlogUpdateForm(request.POST, entry)
    if request.method == 'POST' and form.validate():
        form.populate_obj(entry)
        location = request.route_url('blog_entry', id=entry.id, slug=entry.slug)
        return HTTPFound(location=location)
    return {'form': form, 'action': request.matchdict.get('action')}
