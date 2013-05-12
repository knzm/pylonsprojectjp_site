# -*- coding: utf-8 -*-

import os
import sys
import transaction

from sqlalchemy import engine_from_config

from pyramid.paster import (
    get_appsettings,
    setup_logging,
    )

from pylonsprojectjp.models import DBSession, BaseModel
from pylonsprojectjp.apps.auth.models import UserModel, GroupModel
from pylonsprojectjp.apps.blog.models import BlogEntryModel
from pylonsprojectjp.apps.page.models import PageModel

def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri>\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)

def main(argv=sys.argv):
    if len(argv) != 2:
        usage(argv)

    config_uri = argv[1]
    setup_logging(config_uri)
    settings = get_appsettings(config_uri)

    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    BaseModel.metadata.create_all(engine)

    with transaction.manager:
        from pylonsprojectjp.apps.auth.security import get_user_by_username
        if not get_user_by_username("admin"):
            group = GroupModel.get_or_create(group_name=u"admin")
            admin = UserModel(username=u"admin")
            admin.password = u"admin"
            admin.groups.append(group)
            DBSession.add(admin)

        from pylonsprojectjp.apps.page.api import get_page
        if not get_page(()):
            body = u"""\
これはテストサイトです。
`/admin/ </admin/>`_ から管理画面にログインできます。

- ユーザ名: admin
- パスワード: admin
"""
            page = PageModel(url='/', title=u"Pylons Project JP", body=body,
                             template='index.jinja2')
            DBSession.add(page)
