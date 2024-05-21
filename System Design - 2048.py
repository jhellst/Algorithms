# 2048 -> System Design (Pseudocode + some classes):

# Description:
#   - Game with 1 player
#   - 4 possible "moves" -> tilt left, right, up, down
#      - When we "move" in a direction, adjacent boxes that "bump" will combine IF AND ONLY IF they have the same value
#      - Whenever we make a move -> if game is not over, place a "2" in a random, unoccupied cell. -> Apparently, 10% chance that it will be a "4" instead.

#   - Game can end in 2 ways:
#       1) You get a cell to have a value equal to 2048.
#       2) All squares have a value and none are equal to 2048 AND no adjacent cells are equal in value.

# Example: If we tilt phone right, we shift EVERY cell's value to the right, as far as it can go. Start by shifting all numbers starting from the right.
#   - Then, check if game is won or lost.
#   - If neither won nor lost, now place a 2 randomly in one of the empty cells.

# Requirements for designing game:
#   - class Game:
#       - For init, are # rows and columns always the same? -> Assuming yes.
#       - Contains board (2D array) that represents game state.
#       - Class Methods:
#               - move (up, right, down, left) -> can possibly use an enum here to "map" the specific directions.
#               - checkWin(self) -> Checks board to see if it contains a 2048. -> We can also design the game so that whenever we combine cells and create a 2048, we win immediately.
#               - checkLoss(self) -> Checks board to see if it's completely filled with NO 2048 values. -> We can also design it so that a "count" of cells is kept, and we "lose" the game once count reaches total # of cells (assuming we didn't win).

# Classes

class Game:
    def __init__(self, numRows=4, numCols=4) -> # Possibly take numRows, numCols as inputs. Otherwise, we can assume 4x4.
        row = [None] * numCols
        self.board = [row[::] for _ in range(numRows)] # Initialize board with one "2" and one "4", both in random positions.
        #   - Place a 2 and a 4 in random cells. Make sure to prevent duplicate cell.
        self.numberCount = 2

    # Now, we have the board initialized. We can make moves now.

    def check_win(self):
        # Somehow determine if the combined square is equal to 2048. If so, end the game.

    def check_loss(self):
        # return self.numberCount == numRows * numCols

    # Pseudocode for making a move in a single direction -> we'll use "tilt right".
    def tilt_right(self):
        # Iterate through each row, reversed. Starting from the last (far right) index, we'll move each cell as far to the right as possible (as long as the cell to immediate right is "None", we can move it there and make the prev cell == None).
        # Some rules to determine which cells get combined in the case of a tie.

        for r, row in enumerate(self.board):
            curOrder = row[::] # Get contents of current row.
            # We want to "push" all cells to the far right in this case (for each row).
            # Then, combine all cells that are equal and horizontally adjacent. Check for win in this stage.

            # Check if game is won. Then, check if game is lost. If neither, we can continue playing moves.












# 2nd Attempt at System Design Pseudocode:

# 2048 Requirements:
#   - Game board which is 4*4, and starts with two random cells populated.
#   - Player can "tilt" the board in 4 different directions. These are the 4 available moves at any point.
#       - When a tilt occurs -> combine (and double) any values that are touching in that direction and add 1 more "2" value in a random, empty cell.

# Game is single-player.
# Score is maintained as the max value that you've reached in the game board.

# Need to validate when game is 1) won or 2) over
#   - Check this after each move.
#   - You WIN if you can get a single cell's value to equal 2048.
#   - You LOSE if you can't make any more moves AND you haven't won.


# OOP Class Design:

class Game2048:
    def __init__(self):
        self.board = [[[None] * 4] for i in range(4)] # 4*4 2D array.
        self.squares_filled = 0 # Game ends when this reaches 16.
        self.game_over = False

    def start_game(self): # Starts a new game, resets the board and all other stats.
        # Reset self.board.
        # Randomly select 2 unique cells in the board and place a "2" in them. (Technically, there's a 10% chance that there will be a 4 instead).

    def tilt_right() ....
    
    def make_move(self, tilt_direction):
        # Provide 4 different algorithms to process tiling the board in different directions.

        if tilt_direction == R:
            tilt_right()
        # Example for move_tilt_right:
        def move_tilt_right(self):
            # Every cell will move as far to the right as possible, starting with the far right.
            # Then, we want to combine the shifted cells wherever the same value is touching in left/right axis.
            #   - Basically, any horizontally touching cells that are equal will combine. When we tilt right, we'll combine starting from the right moving to the left.

            # To "Move" numbers:
            # For each row:
            #   Initialize pointer at last column index, to store last open cell.
            #   For each column in the row, starting from the last index (right side):
            #       if there's a value in that cell, make current cell == None and move current cell's value to the current pointer location.
            #           -> Then, increment the pointer.

            # To "Combine" numbers:
            # For each row:
            #   Initialize pointer at last column index, to store last open cell.
            #   For each column in the row, starting from the last index (right side):
            #       If there's a value in that cell AND the next value is the same -> combine them and move it to the pointer location. Change the value of the other cell to None.
            #           -> Then, increment the pointer.
            # Important: At each combine, keep track of score (compare score with value of every newly combined cell). If it ever reaches 2048, you win.
            #   - If you don't win -> check for loss -> this will check if there are 0 empty cells left in the board.

            # After each move -> combine:
            # 1) Re-process score to be the max of current_score and the value of the newly combined cell.
            # 2) Check to see if we've won.
            # 3) If game isn't over, add another "2" to a randomly selected empty space in the board.
            # 5) Check to see if we've lost (the board is filled and there are NO adjacent cells of equal value).
            # 6) Allow for another move to be made.

    # Methods:
    #   - start_game()
    #   - check_win()
    #   - check_loss()
    #   - move()
    #       - separate logic for tilting your phone up, down, left, and right.


# Questions to ask:
# 1) Do we need to provide score-tracking for multiple games, or a max score?
# 2) Is there any specific output that you'd like to see after moves, winning, or losing?


# Marcus' short solution

# Design 2048

# Class
#
# You need a class for the GAME
#   Has a board with a state
#   Has a single player
#   Has a score (max square)

# A player can make one of four "moves": tilt .... r, l, u, d (public)
#    > tilt to right, means combine to the right
#        > 2, 4, 4, 4 RIGHT x, 2, 4, 8
#        > 4, 4, 4, 4 RIGHT x, x, 8, 8 (correct, requires tilt again to get 16)
#            > At the end of tilting the board, one of the empty squares (randomly) becomes a 2
# Once a move is made the class needs ...
#    > logic to update the state of the board after the move
#    > logic to determine if the game is over

class Direction:

class MoveButton:
     public MoveButton(dir):
        self.dir = dir
        self.text = dir.toText()
    
# 4 move_button(s)  -> calls Game.make_move(dir)

class Game2048

    public Game(player?)
         # create a 4x4 board whose values are integers (see properties) 
         # with 2 of the spots (randomly) on the board containing 2s

    private properties
        current_score # max val on board
        board = [[]] # 4x4, int
        player?

   public method(s)
       make_move (tilt) parameters (direction) # be efficient and update the max score as we calculate the new board state
            # looks repetitive, can I use a data structure like a dict to make more terse and efficient?
            case tilt:
                L:
                    generic_tilt(/*x=*/True, /*y=*/False, /*start=*/True) # LEFT
                R:
                    generic_tilt(/*x=*/True, /*y=*/False, /*start=*/False) # RIGHT
                U: ...
                D: ...
          # first make the move and update state, keeping track of max value after combining
          # diplay_board()
               # uses game_over() to determine if it needs to say game over (not allow user to make moves)
           

   private methods
       # Example, how to tilt left by calling generic_tilt?
       #    generic_tilt(/*x=*/True, /*y=*/False, /*start=*/True) # LEFT
       #    generic_tilt(/*x=*/True, /*y=*/False, /*start=*/False) # RIGHT
       generic_tilt : x (bool), y (bool), start (bool)
       game_over : true | false 
       display_board

     
   

