# -*- coding: utf-8 -*-

from webhelpers.paginate import Page

import transaction
from pylonsprojectjp.models import DBSession
from .interfaces import IAdmin

__all__ = [
    'get_model_names',
    'get_admin',
    'get_model',
    'get_page',
    'create_instance',
    'update_instance',
]


def get_model_names(request):
    return [name for name, _ in
            request.registry.getAdapters((request,), IAdmin)]


def get_admin(request, name):
    return request.registry.queryAdapter(request, IAdmin, name=name)


def get_model(request, name):
    admin = get_admin(request, name)
    if info is None:
        return None
    return admin.model_class


def get_page(request, model, page=1, items_per_page=20):
    query = DBSession.query(model)
    return Page(query, page=page, items_per_page=items_per_page)


def create_instance(request, admin, params):
    with transaction.manager:
        instance = admin.model_class(**params)
        DBSession.add(instance)


def update_instance(request, admin, instance, params):
    with transaction.manager:
        instance.from_dict(params)
        DBSession.add(instance)
