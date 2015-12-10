"""
The view functions for the interface app.
"""
from django.core.urlresolvers import reverse
from django.test import TestCase


class TestHomePage(TestCase):
    def test_home_page_renders_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')


class TestGamePage(TestCase):
    def test_game_page_renders_game_template(self):
        response = self.client.get(reverse('game'))
        self.assertTemplateUsed(response, 'game.html')
