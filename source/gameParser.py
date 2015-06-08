from gamePiece import GamePiece
from gameLogger import logger

"""
Contains a set of methods to help create a GameBoard from
an input file.
Sample File:

1 . .
. . .
. . 2

or

1..1
2.X2
3x.3
"""


class GameParser:

    @staticmethod
    def ConvertCharToPlayer(iChar):
        """
        Method used to take an input character from a level
        and assign a player to it.
        One approach to a switch statement in python:
        http://www.pydanny.com/why-doesnt-python-have-switch-case.html

        Args: iChar - Character to convert to player.
        Return: The owning player.
        """
        return {
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            'x': 0,
            'X': 0,
        }.get(iChar, 0)

    @staticmethod
    def IsPiece(iChar):
        """
        Method used to determine if a character is a piece.
        Currently, everything besides an empy space is
        considered a piece.

        Args: iChar - Input character to be considered.
        Return: If it is a piece.
        """
        return {
            '.': False,
        }.get(iChar, True)

    @staticmethod
    def ParseFile(iFile, oGameBoard):
        """
        Method used to parse in input file and
        populate a gameboard object with various game elements.
        TODO: Needs to populate a number of player objects.

        Args:
            iFile - Level file to parse.
            oGameBoard - Fully populated gameboard object.
        """
        file = open(iFile, "r")

        # Operate over each line of the passed file and look for GamePieces.
        height = 0
        width = 0
        for line in file.readlines():
            width = 0
            for char in line.split():
                # When one is found, add to the GameBoard.
                if (GameParser.IsPiece(char)):
                    newPiece = GamePiece(GameParser.ConvertCharToPlayer(char),
                                         width,
                                         height,
                                         char)
                    oGameBoard.AddPiece(newPiece)
                width += 1
            height += 1

        # TODO - This has a potential bug if a non-rectangular level is used.
        # Would have to calculate a max length and width, and use that.
        # Or just do things differently. Or fill all non-rectangular areas with Xs.
        oGameBoard.width = width
        oGameBoard.height = height

        logger.debug("Parsed level name=%s with width=%u height=%u", iFile, width, height)
