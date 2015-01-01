from zope.formlib import form
from zope.interface import implements
from plone.app.portlets.portlets import base
from plone.portlets.interfaces import IPortletDataProvider
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class IEthiopiaLogoPortlet(IPortletDataProvider):
    """ A portlet for the Ethiopia logo. """


class Assignment(base.Assignment):

    implements(IEthiopiaLogoPortlet)


class Renderer(base.Renderer):
    _template = ViewPageTemplateFile('ethiopia-logo.pt')

    def render(self):
        return self._template()


class AddForm(base.AddForm):
    form_fields = form.Fields(IEthiopiaLogoPortlet)


class EditForm(base.EditForm):
    form_fields = form.Fields(IEthiopiaLogoPortlet)
