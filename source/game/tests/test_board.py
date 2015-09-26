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
