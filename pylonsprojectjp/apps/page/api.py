# -*- coding: utf-8 -*-

from pylonsprojectjp.models import DBSession

from .models import PageModel


def get_page(url):
    return DBSession.query(PageModel).filter_by(url=url).first()
