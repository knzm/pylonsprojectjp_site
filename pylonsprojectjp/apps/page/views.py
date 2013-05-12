# -*- coding: utf-8 -*-

from pyramid.httpexceptions import HTTPNotFound
from pyramid.view import view_config
from pyramid.renderers import RendererHelper

from docutils.core import publish_parts

from .api import get_page


@view_config(route_name="page")
def page_view(request):
    subpath = request.matchdict["subpath"]
    page = get_page(subpath)
    if page is None:
        raise HTTPNotFound

    renderer_name = "pylonsprojectjp:templates/page/" + page.template

    helper = RendererHelper(
        name=renderer_name,
        registry=request.registry)

    content = publish_parts(page.body, writer_name='html')['html_body']

    value = {
        "title": page.title,
        "content": content,
        }

    return helper.render_to_response(
        value, None, request=request)
