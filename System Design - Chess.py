# System Design - Chess:
#   - Answers pseudocoded, with some classes/data structures outlined in Python.

# Chess

# Requirements:
#   - Game board with 2 players -> every game will begin with the same board state.
#   - Ability for each player to "move" during their turn. This will allow them to make any legal move with any of their pieces on the board.
#   - For each piece, we have a different set of rules that determine which moves are currently valid.
#       - Example: rooks can only move in a straight line, bishops only diagonal, knights go in "L" shape but can "hop" over other pieces (unlike others).
#   - Functionality for the game to automatically determine if a move triggers "check" or "checkmate".
#   - Ability to restart the game.


# Questions:
#   - Do we want functionality to track multiple games and their results? -> Assume no.
#   - Is the main use case to enable 2 human players to play? -> Yes.


# OOP Design:

class ChessGame:
    def __init__(self, players: list):
        row = [None] * 8
        self.board = [row for i in range(8)] # Board is a 2D array, exactly 8*8 squares. Each cell may contain a piece or None.
        # Upon starting game, the board will be re-set. The pieces will be placed at their original spaces.
        self.color = "white" # Starts as white, then switches to black (and back-and-forth afterwards).
        self.turnNumber = 1 # Increments each time after black's turn.
        self.players = players
        self.is_won = False # Boolean

        self.pieces = {"white": {}, "black": {}} # Holds all pieces for each color with their coords. Removes them when a piece is taken.

    # Methods:

    # Methods needed to validate moves.

class Piece: # Represents a chess piece.
    def __init__(self, color: str, type: str):
        self.color = color
        self.type = type


# Specific pieces will extend the Piece class.


class Rook(Piece):


    def move_rook(self, r, c): # Attempts to move the piece to a specified spot on the board. For each piece, logic will be different.
        # Logic to move the piece. Must validate whether the move is valid. Also need to determine check/checkmate and if a piece is taken.

