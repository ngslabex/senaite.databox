# -*- coding: utf-8 -*-

from bika.lims import api
from senaite.core.z3cform.widgets.datagrid import DataGridWidgetFactory
from plone.app.layout.viewlets import ViewletBase
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from z3c.form.interfaces import INPUT_MODE


class ParamsDatagridViewlet(ViewletBase):
    """Params Datagrid Viewlet
    """

    index = ViewPageTemplateFile("templates/params.pt")

    @property
    def databox(self):
        return self.context

    def update(self):
        """Renders the viewlet and handles form submission
        """
        return self.index()

    def render_field(self):
        field = api.get_fields(self.context)["params"]
        value = field.get(self.context)
        widget = DataGridWidgetFactory(field, self.request)
        widget.mode = INPUT_MODE
        return widget.render()
