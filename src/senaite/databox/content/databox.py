# -*- coding: utf-8 -*-
#
# This file is part of SENAITE.DATABOX.
#
# SENAITE.DATABOX is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation, version 2.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc., 51
# Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# Copyright 2018-2025 by it's authors.
# Some rights reserved, see README and LICENSE.

from plone.dexterity.content import Item
from senaite.databox import _
from senaite.databox.config import DEFAULT_PARAMS
from senaite.databox.interfaces import IDataBox
from zope.interface import implementer
from senaite.core.schema.fields import DataGridRow
from senaite.core.z3cform.widgets.datagrid import DataGridWidgetFactory
from plone.autoform import directives
from zope import schema
from zope.interface import Interface


class IParamsRecordSchema(Interface):
    """DataGrid Row for Params settings
    """

    name = schema.TextLine(
        title=_(u"label_param_name", default=u"Name"),
        description=_(u"Name of parameter"),
        required=False,
    )

    value = schema.TextLine(
        title=_(u"label_param_value", default=u"Value"),
        description=_(u"Value of parameter"),
        required=False,
    )


@implementer(IDataBox)
class DataBox(Item):
    """Intelligent Query Folder
    """

    directives.widget(
        "params",
        DataGridWidgetFactory,
        allow_insert=False,
        allow_delete=True,
        allow_reorder=False,
        auto_append=True)
    # directives.omitted(IAddForm, "params")
    params = schema.List(
        title=_(u"label_params", default=u"Static parameters"),
        description=_(u"description_params",
                      default=u"Static params for use in the columns tab"),
        value_type=DataGridRow(schema=IParamsRecordSchema),
        required=False,
        default=DEFAULT_PARAMS
    )
