# -*- coding: utf-8 -*-

from pyramid.view import view_config, view_defaults
from pyramid.httpexceptions import HTTPForbidden, HTTPNotFound, HTTPFound

from formencode.api import Invalid

from .api import (
    get_admin,
    get_model,
    get_page,
    create_instance,
    update_instance,
    )


@view_config(route_name='admin_dashboard', layout='admin', permission='view',
             renderer='pylonsprojectjp:templates/admin/dashboard.mako')
def admin_dashboard_view(request):
    return {}


@view_defaults(layout="admin", permission='view')
class AdminView(object):
    def __init__(self, context, request):
        self.context = context
        self.request = request

        # from js import jquery_tablesorter
        # jquery_tablesorter.tablesorter.need()
        # jquery_tablesorter.blue.need()

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

    def get_instance(self, model, id):
        return model.get_by_id(id)

    @view_config(route_name='admin_index', request_method='GET',
                 renderer='pylonsprojectjp:templates/admin/list.mako')
    def admin_list_view(self):
        model_name = self.request.matchdict['model']
        admin = get_admin(self.request, model_name)
        if admin is None:
            raise HTTPNotFound('No such model')

        page = self.get_page(admin.model_class)
        return {
            "page_title": admin.title,
            "page": page,
            "grid_data": {
                "model_name": model_name,
                "model_class": admin.model_class,
                "columns": admin.list_columns,
                "items": page.items,
                },
            }

    @view_config(route_name='admin_entry', request_method='GET',
                 renderer='pylonsprojectjp:templates/admin/show.mako')
    def admin_detail_view(self):
        model = self.get_model(self.request.matchdict['model'])
        instance = self.get_instance(model, self.request.matchdict['id'])
        return {"instance": instance, "model": model}

    @view_config(route_name='admin_new',
                 renderer='pylonsprojectjp:templates/admin/new.mako')
    def admin_new_view(self):
        matchdict = self.request.matchdict

        admin = get_admin(self.request, matchdict['model'])
        form = admin.get_form(None)

        value = {}
        if self.request.POST:
            try:
                params = form.validate(self.request.POST)
            except Invalid:
                value = self.request.POST
            else:
                create_instance(self.request, admin, params)
                index_url = self.request.route_url(
                    'admin_index', model=matchdict['model'])
                raise HTTPFound(index_url)

        return {
            "page_title": admin.title,
            "form": form,
            "value": value,
            }

    @view_config(route_name='admin_edit',
                 renderer='pylonsprojectjp:templates/admin/edit.mako')
    def admin_edit_view(self):
        matchdict = self.request.matchdict

        admin = get_admin(self.request, matchdict['model'])
        instance = self.get_instance(admin.model_class, matchdict['id'])
        form = admin.get_form(instance)

        value = {}
        if self.request.POST:
            try:
                params = form.validate(self.request.POST)
            except Invalid:
                value = self.request.POST
            else:
                update_instance(self.request, admin, instance, params)
                index_url = self.request.route_url(
                    'admin_index', model=matchdict['model'])
                raise HTTPFound(index_url)
        else:
            value = instance.to_dict()

        return {
            "page_title": admin.title,
            "form": form,
            "value": value,
            }
