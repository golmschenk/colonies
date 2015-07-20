"""Main execution file."""
from game_board import GameBoard
from game_parser import GameParser
from game_logger import logger
import sys


def main(argv):
    """
    Method that gets executed to run a game of colonies.
    :param argv: Passed argument list to program. File to parse.
    :type argv: list
    """
    if len(argv) < 2:
        logger.error("ERROR - Need to supply file as input.")
        return

    # Parse the provided file into a GameBoard object.
    sample_game_board = GameBoard()
    GameParser.parse_file(argv[1], sample_game_board)

    # Display the resulting GameBoard object in text form.
    sample_game_board.display_text_board()

main(sys.argv)
