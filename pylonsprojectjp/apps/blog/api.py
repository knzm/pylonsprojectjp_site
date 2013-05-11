# -*- coding: utf-8 -*-

from webhelpers.paginate import PageURL_WebOb, Page

from .models import BlogEntryModel


def get_paginator(request, page=1, items_per_page=5):
    page_url = PageURL_WebOb(request)
    query = BlogEntryModel.query()
    return Page(query, page, url=page_url, items_per_page=items_per_page)
