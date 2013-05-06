# -*- coding: utf-8 -*-

from webhelpers.html.grid import ObjectGrid
from pyramid_layout.panel import panel_config

from .api import get_model_names
from .interfaces import IAdminFormInfo


@panel_config('admin_menu', renderer='pylonsprojectjp:templates/admin/panels/menu.mako')
def menu_panel(context, request):
    items = []

    for model_name in sorted(get_model_names(request)):
        url = request.route_url('admin_index', model=model_name)

        title = None
        info = request.registry.queryUtility(IAdminFormInfo, model_name)
        if info:
            title = getattr(info, 'title', None)
        if title is None:
            title = model_name

        items.append({"url": url, "title": title})

    return {"items": items}


@panel_config('admin_buttons', renderer='pylonsprojectjp:templates/admin/panels/admin_buttons.mako')
def buttons_panel(context, request):
    return {}


@panel_config('pager', renderer='pylonsprojectjp:templates/admin/panels/pager.mako')
def pager_panel(context, request, page):
    return {}


@panel_config('grid', renderer='pylonsprojectjp:templates/admin/panels/grid.mako')
def grid_panel(context, request, data):
    grid = ObjectGrid(data['items'], data['columns'])
    return {"grid": grid}
