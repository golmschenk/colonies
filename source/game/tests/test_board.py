"""Items related to testing the board class."""
import pytest
from source.game.board import Board


class TestBoard:
    """Tests for the Board class."""

    def test_add_piece_increases_piece_count(self):
        """
        Test that the add_piece function increases the number of pieces.
        """
        board = Board()
        pre_piece_count = len(board.pieces)

        board.add_piece(1)
        post_piece_count = len(board.pieces)

        assert post_piece_count == pre_piece_count + 1

    def test_add_zone_increases_zone_count(self):
        """
        Test that the add_zone function increases the number of zones.
        """
        board = Board()
        pre_zone_count = len(board.zones)

        board.add_zone(1)
        post_zone_count = len(board.zones)

        assert post_zone_count == pre_zone_count + 1

    def test_add_player_increases_player_count(self):
        """
        Test that the add_player function increases the number of players.
        """
        board = Board()
        pre_player_count = len(board.players)

        board.add_player(1)
        post_player_count = len(board.players)

        assert post_player_count == pre_player_count + 1