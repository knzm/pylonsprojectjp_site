# -*- coding: utf-8 -*-

class BasicLayout(object):
    page_title = 'Pylons Project JP'

    def __init__(self, context, request):
        self.context = context
        self.request = request
        self.home_url = request.application_url
