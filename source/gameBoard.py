
class GameBoard:
    """GameBoard describes the area where a game is played. """

    numBoards = 0

    def __init__(self, iWidth=0, iHeight=0):
        """
        Constructor for a GameBoard.
        Args:
            iWidth - The width of the board.
            iHeight - The height of the board.
        """
        self.width = iWidth
        self.height = iHeight
        self.numBoards += 1
        self.pieces = []

    def AddPiece(self, iPiece):
        """ Method that adds a piece to the pieces list."""
        self.pieces.append(iPiece)

    def DisplayTextBoard(self):
        """Displays the game board in text format."""
        displayString = ""

        # Operate over a copy of the list of pieces.
        # Could sort by y & x to save a lot of time.
        tempPieces = self.pieces
        for y in range(self.height):
            for x in range(self.width):

                # Attempt to find a piece for the new slot.
                pieceFound = False
                for piece in tempPieces:
                    if ((piece.width == x) and (piece.height == y)):
                        displayString += str(piece.type)
                        tempPieces.remove(piece)
                        pieceFound = True

                # If a piece hasn't been found, place an empty space.
                if (pieceFound is False):
                    displayString += '.'
                displayString += ' '
            displayString += '\n'
        print(displayString)
