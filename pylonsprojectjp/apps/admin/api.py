# -*- coding: utf-8 -*-

from webhelpers.paginate import Page

from pylonsprojectjp.models import DBSession
from .interfaces import IAdminFormInfo


def get_model_names(request):
    return [name for name, _ in
            request.registry.getUtilitiesFor(IAdminFormInfo)]


def get_form_info(request, model_name):
    return request.registry.queryUtility(IAdminFormInfo, model_name)


def get_model(request, model_name):
    info = get_form_info(request, model_name)
    if info is None:
        return None
    return info.model_class


def get_page(request, model, page=1, items_per_page=20):
    query = DBSession.query(model)
    return Page(query, page=page, items_per_page=items_per_page)

