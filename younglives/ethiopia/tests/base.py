from plone.app.testing import PloneSandboxLayer
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting

from plone.testing import z2

from younglives.ethiopia.config import PROJECTNAME


class TestCase(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import plone.app.theming
        self.loadZCML(package=plone.app.theming)
        import younglives.theme
        self.loadZCML(package=younglives.theme)
        import younglives.ethiopia
        self.loadZCML(package=younglives.ethiopia)

        # Install product and call its initialize() function
        z2.installProduct(app, PROJECTNAME)

    def setUpPloneSite(self, portal):
        # Install into Plone site using portal_setup
        self.applyProfile(portal, '%s:default' % PROJECTNAME)

    def tearDownZope(self, app):
        # Uninstall product
        z2.uninstallProduct(app, PROJECTNAME)

FIXTURE = TestCase()
INTEGRATION_TESTING = IntegrationTesting(
    bases=(FIXTURE,), name="fixture:Integration")
