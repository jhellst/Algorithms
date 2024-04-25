# 2048 -> System Design (Pseudocode + some classes):

# Description:
#   - Game with 1 player
#   - 4 possible "moves" -> tilt left, right, up, down
#      - When we "move" in a direction, adjacent boxes that "bump" will combine IF AND ONLY IF they have the same value.
#      - Whenever we make a move -> if game is not over, place a "2" in a random, unoccupied cell. -> Apparently, 10% chance that it will be a "4" instead.

#   - Game can end in 2 ways:
#       1) You get a cell to have a value equal to 2048.
#       2) All squares have a value and none are equal to 2048.

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
