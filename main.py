"""Main execution file."""
from game import Game
from player import Player
from unit import Unit

# Initialize the game.
game = Game()

# Create a 5x10 board.
game.create_empty_board(5, 10)

# Add two players.
game.players.append(Player())
game.players.append(Player())

# Create a unit for each player.
game.board[0][0] = Unit(game.players[0])
game.board[5][1] = Unit(game.players[1])

# Display the board.
game.display_board()
