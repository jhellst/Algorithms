# Design Tic Tac Toe
# Focus on Pseudocode. Will structure classes and methods, but not 100% expected to code all of solution.

# Requirements:
#   - Design a tic tac toe game with 2 players and a standard board. For now, just want to do a single game (vs. a match that needs to be tracked).
#   - Upon initialization, we'll have 1) an empty 3x3 board, and 2) 2 players (one "X" and one "O").
#   - Need to track whose turn it is.
#   - Need to have methods for player to place piece. For now we'll just track whose turn it is and force that player to move.

# After each turn:
#   - Method to check board for 1) game won by player or 2) board full, no winner.

# Display? Or just underlying system? -> Just underlying system for now.
# Scaling? None, for now.
# How to track players? -> Just player1 and player2 for now.

# Starting to pseudocode a design.

class TicTacToe:
    def __init__(self, player1="p1", player2="p2"):
        self.board = [[None, None, None], [None, None, None], [None, None, None]] # Create the entire empty board here. None represents empty spaces.
        self.player1 = [player1, "X"] # [player, piece (x or o)]
        self.player2 = [player2, "O"]
        self.currentTurn = self.player1
        self.piecesPlaced = 0

    # This should initialize the empty board with both players, turn starting with p1.
    # Now we can start playing the game.
    #   - Each time a piece is played, the board must be evaluated for winning. If game isn't over, switch to other player.

    def checkWin(self, r, c): # Checks a specific coord to determine if we just made 3 in a row.
        # Try to make 3 in a row going up, down, left, right, diag (x2). If found, call endGame.
        # If not found, call checkTie.

        if win: # Condition where winning is true.
            print(self.currentTurn[0] + "wins!")
            self.endGame()
        else:
            self.checkTie()

    def checkTie(self): # Called ONLY if checkWin is called and game is not over.
        if self.piecesPlaced == 9:
            # If all board spaces are taken and not a win, we have a tie. Print tie output.
            print("Tie")
            self.endGame()

    def placePiece(self, piece, r, c): # Places a piece (X or O) at the specified coordinates of the board. Need to prevent from placing in filled spot.
        if self.board[r][c]:
            return
            # Error.
        self.board[r][c] = piece
        self.piecesPlaced += 1

        # Check for win AND tie.
        self.checkWin(r, c)

        # Switch turns.
        if self.currentTurn == self.player1:
            self.currentTurn = self.player2
        else:
            self.currentTurn = self.player1

    def endGame(self):
        # Ends the game and prints the final board.
        print(self.board)
        print("Game over!")