"""
The view functions for the interface app.
"""
from bs4 import BeautifulSoup
from unittest.mock import patch, Mock

from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpRequest
from django.test import TestCase

from interface.views import NewGameView


class TestHomePage(TestCase):
    def test_home_page_renders_home_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')


class TestNewGamePage(TestCase):
    @patch('interface.views.reverse')
    @patch('interface.views.Game')
    def test_creates_game(self, mock_game_class, mock_reverse):
        response = self.client.get(reverse('new-game'))
        assert mock_game_class.objects.create.called

    @patch('interface.views.Game.objects.create')
    def test_generates_correct_url_to_game_with_new_game_id(self, mock_create):
        mock_game = Mock()
        mock_game.id = 2
        mock_create.return_value = mock_game

        new_game_view = NewGameView()
        url = new_game_view.get_redirect_url()

        assert url == reverse('game', kwargs={'game_id': mock_game.id})



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
