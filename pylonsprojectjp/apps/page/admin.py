# -*- coding: utf-8 -*-

from tw2.forms import (
    TableForm,
    TextField,
    TextArea,
    LabelField,
    SingleSelectField,
    )

from pylonsprojectjp import validators
from pylonsprojectjp.apps.admin import (
    admin_config,
    ListColumn,
    )

from .models import PageModel


class PageForm(TableForm):
    id = LabelField(
        label=u"ID",
        css_class='input-xxlarge',
        validator=validators.Int)
    url = TextField(
        label=u"URL",
        css_class='input-xxlarge',
        validator=validators.UnicodeString(not_empty=True))
    title = TextField(
        label=u"タイトル",
        css_class='input-xxlarge',
        validator=validators.UnicodeString(max=255, strip=True))
    body = TextArea(
        label=u"本文",
        css_class='input-xxlarge', rows=10,
        validator=validators.UnicodeString)
    template = SingleSelectField(
        label=u"テンプレート",
        css_class='input-xxlarge',
        options=[('index.jinja2', u"トップページ"),
                 ('page.jinja2', u"通常ページ")],
        validator=validators.OneOf(['index.jinja2', 'page.jinja2'],
                                   not_empty=True))


@admin_config(name='page')
class PageAdmin(object):
    title = u"ページ管理"

    list_columns = [
        ListColumn('id', label=u"ID"),
        ListColumn('url', label=u"URL"),
        ListColumn('title', label=u"タイトル"),
        # ListColumn('body', label=u"本文"),
        ListColumn('created', label=u"作成日時"),
        ListColumn('modified', label=u"更新日時"),
        ]

    model_class = PageModel

    def __init__(self, request):
        self.request = request

    def get_form(self, entity):
        return PageForm()
