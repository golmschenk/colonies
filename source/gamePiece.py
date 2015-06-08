from enum import Enum

"""
Contains GamePiece object, which represents a single piece of a game.
"""


"""
I don't know if we need this or want this.  I'm not sure I want 
to represent pieces based on what they appear in the input file.
This implies that each player can only have one type of piece.
I don't want to have that restriction.

class GameElementType(Enum):
    player1Piece = '1'
    player2Piece = '2'
    player3Piece = '3'
    player4Piece = '4'
    block = 'X'
    empty = '.'
"""

class GamePiece:

    def __init__(self, iPlayer, iWidth, iHeight, iType):
        """
        Constructor for GamePiece class.

        Args:
            iPlayer - The player which controls this piece.
                      Player 0 implies no player.
            iWidth  - The X coordinate of the piece.
            iHeight - The Y coordinate of the piece.
            iType   - What type of piece it is.
        """
        self.player = iPlayer
        self.width = iWidth
        self.height = iHeight
        self.type = iType