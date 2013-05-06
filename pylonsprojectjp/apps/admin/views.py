# -*- coding: utf-8 -*-

from pyramid.view import view_config, view_defaults
from pyramid.httpexceptions import HTTPForbidden, HTTPNotFound

from .api import get_form_info, get_model, get_page


@view_config(route_name='admin_dashboard', layout='admin',
             renderer='pylonsprojectjp:templates/admin/dashboard.mako')
def admin_dashboard_view(request):
    return {}


@view_defaults(layout="admin")
class AdminView(object):
    def __init__(self, context, request):
        self.context = context
        self.request = request

    def get_model(self, model_name):
        return get_model(self.request, model_name)

    def get_page(self, model):
        args = {}

        page = self.request.params.get('page')
        if page:
            args["page"] = int(page)

        items_per_page = self.request.params.get('items_per_page')
        if items_per_page:
            args["items_per_page"] = int(items_per_page)

        return get_page(self.request, model, **args)

    def get_entry(self, model, id):
        return model.get_by_id(id)

    @view_config(route_name='admin_index', request_method='GET',
                 renderer='pylonsprojectjp:templates/admin/list.mako')
    def admin_list_view(self):
        info = get_form_info(self.request, self.request.matchdict['model'])
        if info is None:
            raise HTTPNotFound('No such model')
        page = self.get_page(info.model_class)
        return {
            "page_title": info.title,
            "page": page,
            "grid_data": {"columns": info.list_columns, "items": page.items},
            }

    @view_config(route_name='admin_entry', request_method='GET',
                 renderer='pylonsprojectjp:templates/admin/show.mako')
    def admin_detail_view(self):
        model = self.get_model(self.request.matchdict['model'])
        entry = self.get_entry(model, self.request.matchdict['id'])
        return {"entry": entry, "model": model}
