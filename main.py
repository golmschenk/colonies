"""Main execution file."""
from source.game.board import Board
from source.game.parser import Parser
from source.game.logger import logger
from source.game.console import Console
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

    # Parse the provided file into a Board object.
    sample_game_board = Board()
    Parser.parse_file(argv[1], sample_game_board)

    # Play a game of Colonies with the newly created board.
    console = Console(sample_game_board)
    console.play()

main(sys.argv)
