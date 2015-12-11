"""
The view functions for the interface app.
"""
from bs4 import BeautifulSoup

from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpRequest
from django.test import TestCase

from interface.views import GameView


class TestHomePage(TestCase):
    def test_home_page_renders_home_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')


class TestGamePage(TestCase):
    def test_game_page_renders_game_template(self):
        response = self.client.get(reverse('game'))
        self.assertTemplateUsed(response, 'game.html')

    def test_template_has_no_table_cells_when_there_is_no_board_argument(self):
        response = render(HttpRequest(), 'game.html')
        soup = BeautifulSoup(response.content, 'html.parser')
        board_table = soup.find(id='board_table')
        assert 'td' not in str(board_table)

    def test_template_has_table_cells_when_there_is_a_board_argument(self):
        board_rows = ['1.2']
        response = render(HttpRequest(), 'game.html', context={'board_rows': board_rows})
        soup = BeautifulSoup(response.content, 'html.parser')
        board_table = soup.find(id='board_table')
        assert 'td' in str(board_table)
