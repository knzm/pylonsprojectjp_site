# -*- coding: utf-8 -*-

from formencode import validators
from tw2.forms import (
    TableForm,
    TextField,
    TextArea,
    LabelField,
    )
from tw2.tinymce import TinyMCEWidget

from pylonsprojectjp.apps.admin import (
    admin_config,
    ListColumn,
    )

from .models import BlogEntryModel


class BlogEntryForm(TableForm):
    id = LabelField(
        label=u"ID",
        validator=validators.Int)
    title = TextField(
        label=u"タイトル",
        validator=validators.UnicodeString(max=255, strip=True))
    body = TinyMCEWidget(
        label=u"本文",
        validator=validators.UnicodeString)


@admin_config(name='blog')
class BlogAdmin(object):
    title = u"ブログ管理"

    list_columns = [
        ListColumn('id', label=u"ID"),
        ListColumn('title', label=u"タイトル"),
        ListColumn('body', label=u"本文"),
        ListColumn('created', label=u"作成日時"),
        ListColumn('modified', label=u"更新日時"),
        ]

    model_class = BlogEntryModel

    def __init__(self, request):
        self.request = request

    def get_form(self, entity):
        return BlogEntryForm()
