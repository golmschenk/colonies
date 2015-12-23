"""
The view functions for the interface app.
"""
import pickle
from unittest.mock import Mock, patch

from django.test import TestCase

from interface.models import Game


class TestGameModel(TestCase):
    def test_can_save_and_retrieve_with_pickled_data(self):
        game = Game()
        data = '12345'
        game.data = pickle.dumps(data)

        game.save()
        saved_game = Game.objects.first()

        assert pickle.loads(saved_game.data) == data

    @patch('interface.models.pickle.loads')
    def test_can_retrieve_the_game_board_from_game_data(self, mock_loads):
        game = Game()
        game_data = Mock()
        game_data.board = '1..\n...\n..2'
        mock_loads.return_value = game_data

        board_rows = game.board_rows

        assert board_rows == ['1..', '...', '..2']

    @patch('interface.models.pickle.loads')
    def test_can_retrieve_the_game_status_from_game_data(self, mock_loads):
        game = Game()
        game_data = Mock()
        game_data.status = 'status string'
        mock_loads.return_value = game_data

        game_status = game.status

        assert game_status == 'status string'

    @patch('interface.models.CoreGame')
    def test_game_manager_creates_with_core_game_object_default_put_into_data(self, mock_core_game_class):
        mock_core_game = 'fake core game'
        mock_core_game_class.return_value = mock_core_game

        game = Game.objects.create_game()

        assert game == Game.objects.first()
        assert pickle.loads(game.data) == mock_core_game

    @patch('interface.models.pickle.dumps')
    @patch('interface.models.pickle.loads')
    def test_move_calls_datas_move(self, mock_loads, mock_dumps):
        mock_core_game = Mock()
        mock_loads.return_value = mock_core_game
        mock_dumps.return_value = 'dumps return'
        game = Game()
        game.data = 'game data'

        game.move(current_x=1, current_y=2, new_x=3, new_y=4)

        assert mock_loads.call_args == (('game data',), {})
        assert mock_core_game.move.called
        assert mock_core_game.move.call_args == ((), {'current_x': 1, 'current_y': 2, 'new_x': 3, 'new_y': 4})
        assert game.data == 'dumps return'
