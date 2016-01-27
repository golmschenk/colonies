"""
The base functional test to be subclassed for other functional tests.
"""
from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase


class BaseFunctionalTest(StaticLiveServerTestCase):
    """
    The base functional test which prepares common things like settings up the browser.
    """
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()