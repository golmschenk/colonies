"""Main execution file."""
from gameBoard import GameBoard
from gameParser import GameParser
import sys


def main(iArgv):
    """
    Method that gets executed to run a game of colonies.
    Args:
        iArgv - Location of a colonies level file to parse and play.
    """
    if len(iArgv) < 2:
        print("ERROR - Need to supply file as input.")
        return

    # Parse the provided file into a GameBoard object.
    sampleGameBoard = GameBoard()
    GameParser.ParseFile(iArgv[1], sampleGameBoard)

    # Display the resulting GameBoard object in text form.
    sampleGameBoard.DisplayTextBoard()

main(sys.argv)
