# -*- coding: utf-8 -*-

from pylonsprojectjp.apps.admin import ListColumn


def includeme(config):
    list_columns = [
        ListColumn('id', label=u"ID"),
        ListColumn('title', label=u"タイトル"),
        ListColumn('body', label=u"本文"),
        ListColumn('created', label=u"作成日時"),
        ListColumn('modified', label=u"更新日時"),
        ]
    config.add_admin_form(
        form_class='.forms.BlogCreateForm',
        model_class='.models.BlogEntryModel',
        name='blog', title=u"ブログ管理",
        list_columns=list_columns)
