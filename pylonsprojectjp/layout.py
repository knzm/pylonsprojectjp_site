# -*- coding: utf-8 -*-

from pyramid_layout.panel import panel_config


class BasicLayout(object):
    page_title = 'Pylons Project JP'

    def __init__(self, context, request):
        self.context = context
        self.request = request
        self.home_url = request.application_url


class AdminLayout(object):
    page_title = 'Admin'
    project_name = 'Pylons Project JP'

    def __init__(self, context, request):
        self.context = context
        self.request = request
        self.home_url = request.application_url

    @property
    def project_url(self):
        return self.request.route_url('home')


@panel_config('menu', renderer='pylonsprojectjp:templates/menu.jinja2')
def menu_panel(context, request):
    def is_active(path):
        return request.path.startswith(path)
    return {
        "is_active": is_active,
        }
