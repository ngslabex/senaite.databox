# -*- coding: utf-8 -*-

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
        return self.context.widget("params", mode=INPUT_MODE)
