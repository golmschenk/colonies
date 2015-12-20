"""
The view functions for the interface app.
"""
from bs4 import BeautifulSoup
from unittest.mock import patch, Mock

from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpRequest
from django.test import TestCase

from interface.views import NewGameView, GameView, MoveView


class TestHomePage(TestCase):
    def test_home_page_renders_home_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')


class TestNewGamePage(TestCase):
    @patch('interface.views.reverse')
    @patch('interface.views.Game')
    def test_creates_game(self, mock_game_class, mock_reverse):
        response = self.client.get(reverse('new-game'))
        assert mock_game_class.objects.create_game.called

    @patch('interface.views.Game.objects.create_game')
    def test_generates_correct_url_to_game_with_new_game_pk(self, mock_create_game):
        mock_game = Mock()
        mock_game.pk = 2
        mock_create_game.return_value = mock_game

        new_game_view = NewGameView()
        url = new_game_view.get_redirect_url()

        assert url == reverse('game', kwargs={'game_pk': mock_game.pk})


class TestGamePage(TestCase):
    @patch('interface.views.get_object_or_404')
    def test_game_page_renders_game_template(self, mock_get_object_or_404):
        response = self.client.get(reverse('game', kwargs={'game_pk': 2}))

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

    @patch('interface.views.get_object_or_404')
    @patch('interface.views.Game')
    def test_game_pk_is_retrieve_by_passed_pk_and_set_in_context(self, mock_game_class, mock_get_object_or_404):
        game_view = GameView()
        mock_game = Mock()
        mock_game.board_rows = ['1.2']
        mock_get_object_or_404.return_value = mock_game

        context = game_view.get_context_data(**{'game_pk': 2})

        assert mock_get_object_or_404.called
        assert mock_get_object_or_404.call_args == ((mock_game_class,), {'pk': 2})
        assert context['board_rows'] == mock_game.board_rows


class TestMovePage(TestCase):
    @patch('interface.views.get_object_or_404')
    def test_redirects_to_game_view_with_passed_game_pk(self, _):
        game_pk = 2
        move_view = MoveView()

        url = move_view.get_redirect_url(game_pk, 0, 0, 0, 0)

        assert url == reverse('game', kwargs={'game_pk': game_pk})

    @patch('interface.views.get_object_or_404')
    @patch('interface.views.Game')
    def test_retrieves_game_and_calls_its_move_with_passed_arguments(self, mock_game_class, mock_get_object_or_404):
        game_pk = 2
        current_x, current_y, new_x, new_y = 1, 2, 3, 4
        move_view = MoveView()
        mock_game = Mock()
        mock_get_object_or_404.return_value = mock_game

        url = move_view.get_redirect_url(game_pk=game_pk, current_x=current_x, current_y=current_y,
                                         new_x=new_x, new_y=new_y)

        assert mock_get_object_or_404.call_args == ((mock_game_class,), {'pk': 2})
        assert mock_game.move.call_args == ((), {'current_x': current_x, 'current_y': current_y,
                                                 'new_x': new_x, 'new_y': new_y})


