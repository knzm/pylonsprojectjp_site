# -*- coding: utf-8 -*-

from tw2.forms import (
    TableForm,
    TextField,
    TextArea,
    LabelField,
    )
from tw2.tinymce import TinyMCEWidget

from pylonsprojectjp import validators
from pylonsprojectjp.apps.admin import (
    admin_config,
    ListColumn,
    )

from .models import PageModel


class PageForm(TableForm):
    id = LabelField(
        label=u"ID",
        validator=validators.Int)
    url = TextField(
        label=u"URL",
        validator=validators.UnicodeString(not_empty=True))
    title = TextField(
        label=u"タイトル",
        validator=validators.UnicodeString(max=255, strip=True))
    body = TinyMCEWidget(
        label=u"本文",
        validator=validators.UnicodeString)


@admin_config(name='page')
class PageAdmin(object):
    title = u"ページ管理"

    list_columns = [
        ListColumn('id', label=u"ID"),
        ListColumn('url', label=u"URL"),
        ListColumn('title', label=u"タイトル"),
        ListColumn('body', label=u"本文"),
        ListColumn('created', label=u"作成日時"),
        ListColumn('modified', label=u"更新日時"),
        ]

    model_class = PageModel

    def __init__(self, request):
        self.request = request

    def get_form(self, entity):
        return PageForm()
