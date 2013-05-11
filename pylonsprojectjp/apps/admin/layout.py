# -*- coding: utf-8 -*-

from pyramid_layout.panel import panel_config

from formalchemy import fatypes
from formalchemy.fields import Field, AttributeField
from formalchemy.tables import Grid

from .api import get_model_names, get_admin
from .interfaces import IAdmin

EDIT_LINK_TEMPLATE = u'''\
<a href="%(url)s" title="%(label)s">%(label)s</a>
'''


@panel_config('admin_menu', renderer='pylonsprojectjp:templates/admin/panels/menu.mako')
def menu_panel(context, request):
    items = []

    for model_name in sorted(get_model_names(request)):
        url = request.route_url('admin_index', model=model_name)

        admin = get_admin(request, model_name)
        if admin:
            title = admin.title
        else:
            title = model_name

        items.append({"url": url, "title": title})

    return {"items": items}


@panel_config('admin_buttons', renderer='pylonsprojectjp:templates/admin/panels/admin_buttons.mako')
def buttons_panel(context, request):
    return {
        "new_button_link": request.route_url("admin_new", model=request.matchdict['model']),
        "new_button_label": "Add",
        }


@panel_config('pager', renderer='pylonsprojectjp:templates/admin/panels/pager.mako')
def pager_panel(context, request, page):
    return {}


@panel_config('grid', renderer='pylonsprojectjp:templates/admin/panels/grid.mako')
def grid_panel(context, request, data):
    model_class = data['model_class']
    grid = Grid(model_class, instances=data['items'])

    fields = []
    for column in data['columns']:
        field = column.field or grid._fields.get(column.name)
        if field is None:
            # field = AttributeField(getattr(model_class, column.name), grid)
            field = Field(column.name, fatypes.String)
        field.set(label=column.label)
        fields.append(field)

    # def checkbox(item):
    #     return u"""<input type="checkbox" name="_check" value="%d" />""" % item.id
    # field = Field('check', fatypes.String, checkbox, label=u"")
    # grid.insert(grid["id"], field)
    # fields.insert(0, field)

    model_name = data['model_name']
    def edit_link(item):
        url = request.route_url('admin_edit', model=model_name, id=item.id)
        return EDIT_LINK_TEMPLATE % dict(url=url, label='Edit')
    field = Field('edit', fatypes.String, edit_link)
    grid.append(field)
    fields.append(field)

    grid.configure(pk=1, include=fields)

    return {"grid": grid, "request": request}
