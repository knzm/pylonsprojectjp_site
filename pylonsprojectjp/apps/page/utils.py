# -*- coding: utf-8 -*-

from .api import get_page


def page_predicate(info, request):
    # subpath = info["match"]["subpath"]
    page = get_page(request.path_info)
    return page is not None
