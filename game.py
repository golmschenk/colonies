"""This file contains the stuff for the overall data of a specific game."""

class Game:
    """The class to hold the game data."""
    def __init__(self):
        """Game object initilizer."""
        self.players = []
        self.board = []

    def create_empty_board(self, height, width):
        """Sets up an empty board of the given size."""
        for x in range(width):
            self.board.append([])  # Add a new row (empty list).
            for y in range(height):
                self.board[-1].append(None)  # Add a space in the new row (None object).

    def display_board(self):
        """Displays the game board."""
        display_string = ""
        for row in self.board:
            for unit in row:
                if unit:  # If position is not empty...
                    display_string += str(unit.owner.id)  # Show the unit's owner id.
                else:
                    display_string += '.'
            display_string += '\n'
        print(display_string)
