# -*- coding: utf-8 -*-

from webhelpers.paginate import PageURL_WebOb, Page

from .models import EntryModel


def get_paginator(request, page=1, items_per_page=5):
    page_url = PageURL_WebOb(request)
    return Page(EntryModel.all(), page, url=page_url, items_per_page=items_per_page)
