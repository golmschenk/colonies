"""Items related to testing the board class."""
import pytest
from source.game.board import Board
from source.game.piece import Piece
from source.game.player import Player
from source.game.zone import Zone


class TestBoard:
    """Tests for the Board class."""

    def test_add_piece_increases_piece_count(self):
        """
        Test that the add_piece function increases the number of pieces.
        """
        board = Board()
        pre_piece_count = len(board.pieces)

        board.add_piece(Piece(0, 0, 0, 0))
        post_piece_count = len(board.pieces)

        assert post_piece_count == pre_piece_count + 1

    def test_add_zone_increases_zone_count(self):
        """
        Test that the add_zone function increases the number of zones.
        """
        board = Board()
        pre_zone_count = len(board.zones)

        board.add_zone(Zone(0, 0, 0))
        post_zone_count = len(board.zones)

        assert post_zone_count == pre_zone_count + 1

    def test_add_player_increases_player_count(self):
        """
        Test that the add_player function increases the number of players.
        """
        board = Board()
        pre_player_count = len(board.players)

        board.add_player(Player(0))
        post_player_count = len(board.players)

        assert post_player_count == pre_player_count + 1

    def test_can_detect_when_player_has_pieces(self):
        """
        Test that the board can detect if a player has pieces remaining.
        """
        board = Board()
        board.pieces = [Piece(0, 0, 0, 0), Piece(2, 2, 2, 2)]

        player_2_has_piece = board.does_player_have_pieces(2)

        assert player_2_has_piece

    def test_can_detect_when_player_has_no_pieces(self):
        """
        Test that the board can detect if a player has no pieces remaining.
        """
        board = Board()
        board.pieces = [Piece(0, 0, 0, 0), Piece(2, 2, 2, 2)]

        player_1_has_piece = board.does_player_have_pieces(1)

        assert not player_1_has_piece
