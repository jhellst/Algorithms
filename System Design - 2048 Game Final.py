from random import randrange
from collections import deque

# 2048 -> Algorithm to solve for

# 2048 is played on a gray 4 × 4 grid with numbered tiles that slide smoothly when a player moves them using one
# of the four arrow keys - Up, Down, Left or Right. On every turn, a new tile with a value of either 2 or 4 randomly appears on
# an empty spot of the board. After one of the keys is pressed, the tiles slide as far as possible in the chosen direction until
# they are stopped either by another tile or by the edge of the grid. If two tiles with the same number collide while moving,
# they merge into a tile with this number doubled. You can't merge an already merged tile in the same turn. If there are more
# than 2 tiles in the same row (column) that can merge, the farthest (closest to an edge) pair will be merged first (see the second example).

# In this problem you are not going to solve the 2048 puzzle, but you are going to find the final state of the board from the given one after
# a defined set of n arrow key presses, assuming that no new random tiles will appear on the empty spots.


# Steps:
#   1) Iterate through all of the "directions" provided in path, one by one
#   2) Upon each directional move, we need to shift all cells in the move direction (L,R,U,D) and combine any blocks of equal value that are touching after the shift.
#       - Note: For L/R move, only want to combine blocks of equal value that are horizontally adjacent.
#       - For every combined block, we want to evaluate that against the current_score. (Your score is the highest value currently in the game board).
#       a) If any of the combined blocks == 2048, we know that we have won the game. -> Display the board, but show a "You Win" message and prevent any additional user input (besides to start a new game).
#       b) If the board is completely full AND there are no adjacent blocks of equal value, you lose -> Display the board, show a "You Lose" message and prevent any additional user input (besides to start a new game).

# User's interaction with the API:
#   - game2048.make_moves(path) -> processes every move in path, and updates the game/board state accordingly.


# Classes and Methods:

# class Game2048:
#   Properties:
#   - board: 2D array of 4*4 dimensions
#       - Upon initialization, need to randomly place 2 2's in random cells.
#   - score: int -> current score (max cell value in board).
#   - game_over: Boolean
#   - game_is_won: Boolean

#   Public Methods:
#   - make_move(direction)
#       -> Makes a move and updates the board state accordingly. Options for direction are: L/R/U/D
#   - start_game(): Resets the board and score for a new game.

#   Private Methods:
#   - _check_win():
#   - _check_loss():


# Class that allows you to provide an initial board state. Processes the board state for each direction provided in "path".
class Game2048:
    def __init__(self, board):
        self.board = board
        self.score = 2 # This will be the max value in the board at any point.
        self.game_over = False
        self.game_is_won = False


    def _check_if_loss(self):

        for row_index in range(0, 4):
            prev = None
            for col_index in range(0, 4):
                if self.board[row_index][col_index] == 0:
                    return False
                if prev and prev == self.board[row_index][col_index]: # We have an adjacent equal cell in the board.
                    return False

        for col_index in range(0, 4):
            prev = None
            for row_index in range(0, 4):
                if self.board[row_index][col_index] == 0:
                    return False
                if prev and prev == self.board[row_index][col_index]: # We have an adjacent equal cell in the board.
                    return False

        return True



    def make_move(self, direction):
        """Processes a single move made by the user. 'Slides' all values in that direction and combines any equal values that collide."""

        # Note: Logic will differ based on the direction. Each "move" will result in a shifting AND a combining step.

        # Tilt phone to the left -> all values slide to the left, but maintain the same row. Then, combine horizontal cells of equal value, prioritizing combining any cells further to the left.


        # Construct each row's deque of values. Then, pop each value while checking to see if we can combine them.
        if direction == "R":
            cur_col_values = deque()
            for row_index in range(0, 4):

                for col_index in range(3, -1, -1):
                    cur_value = self.board[row_index][col_index]
                    self.board[row_index][col_index] = 0

                    if cur_value != 0: # We have a number in this cell.
                        cur_col_values.append(cur_value)

                insert_col_index = 3 # Used to track the location where the next number will shift.
                while cur_col_values:
                    val_to_insert = cur_col_values.popleft()
                    if cur_col_values and cur_col_values[0] == val_to_insert: # If we have the same adjacent value -> combine.
                        cur_col_values.popleft()
                        val_to_insert *= 2
                    self.board[row_index][insert_col_index] = val_to_insert
                    insert_col_index -= 1

        elif direction == "L":
            cur_col_values = deque()
            for row_index in range(0, 4):

                for col_index in range(0, 4):
                    cur_value = self.board[row_index][col_index]
                    self.board[row_index][col_index] = 0

                    if cur_value != 0:
                        cur_col_values.append(cur_value)

                insert_col_index = 0
                while cur_col_values:
                    val_to_insert = cur_col_values.popleft()
                    if cur_col_values and cur_col_values[0] == val_to_insert: # If we have the same adjacent value -> combine.
                        cur_col_values.popleft()
                        val_to_insert *= 2
                    self.board[row_index][insert_col_index] = val_to_insert
                    insert_col_index += 1

        elif direction == "U":
            cur_row_values = deque()
            for col_index in range(0, 4):

                for row_index in range(0, 4):
                    cur_value = self.board[row_index][col_index]
                    self.board[row_index][col_index] = 0

                    if cur_value != 0:
                        cur_row_values.append(cur_value)

                insert_row_index = 0
                while cur_row_values:
                    val_to_insert = cur_row_values.popleft()
                    if cur_row_values and cur_row_values[0] == val_to_insert: # If we have the same adjacent value -> combine.
                        cur_row_values.popleft()
                        val_to_insert *= 2
                    self.board[insert_row_index][col_index] = val_to_insert
                    insert_row_index += 1

        elif direction == "D":
            cur_row_values = deque()
            for col_index in range(0, 4):

                for row_index in range(3, -1, -1):
                    cur_value = self.board[row_index][col_index]
                    self.board[row_index][col_index] = 0

                    if cur_value != 0:
                        cur_row_values.append(cur_value)

                insert_row_index = 3
                while cur_row_values:
                    val_to_insert = cur_row_values.popleft()
                    if cur_row_values and cur_row_values[0] == val_to_insert: # If we have the same adjacent value -> combine.
                        cur_row_values.popleft()
                        val_to_insert *= 2
                    self.board[insert_row_index][col_index] = val_to_insert
                    insert_row_index -= 1


        # Check to see if we've lost the game. The board would be 1) completely filled and 2) no adjacent cells of equal value will exist.
        if not self.game_over:
            self.game_over = self._check_if_loss()

        if self.game_over:
            if self.game_is_won:
                print("You Win!")
            else:
                print("You Lose!")

        # Now, we want to place a random 2 in an empty cell.
        new_two_placed = False
        while not new_two_placed:
            x, y = randrange(0, 4), randrange(0, 4)
            if self.board[x][y] == 0:
                self.board[x][y] = 2
                new_two_placed = True





# def game2048(grid, path):

# Example:
grid = [[0, 0, 0, 0],
        [0, 0, 2, 2],
        [0, 0, 2, 4],
        [2, 2, 4, 8]]

path = "RR"



game = Game2048(grid)
print("Initial BOARD", game.board)
game.make_move("R")
print("ACUTAL BOARD", game.board)
game.make_move("R")
print("ACUTAL BOARD", game.board)

print("EXAMPLE_BOARD", [[0, 0, 0, 0],
                [0, 0, 0, 4],
                [0, 0, 2, 4],
                [0, 0, 8, 8]])





# grid2 = [[2, 2, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
# game2 = Game2048(grid2)
# print("Initial BOARD", game2.board)
# game2.make_move("R")
# print("Actual BOARD", game2.board)
# game2.make_move("L")
# print("Actual BOARD", game2.board)
# game2.make_move("R")
# print("Actual BOARD", game2.board)
# game2.make_move("D")
# print("Actual BOARD", game2.board)


# print(solution(grid, path))

# solution(grid, path) = [[0, 0, 0, 0],
#                         [0, 0, 0, 4],
#                         [0, 0, 2, 4],
#                         [0, 0, 8, 8]]



grid3 = [[2, 0, 0, 0], [2, 0, 0, 0], [4, 0, 0, 0], [0, 0, 0, 0]]
game3 = Game2048(grid3)
print("Initial BOARD", game3.board)
game3.make_move("D")
print("Actual BOARD", game3.board)
game3.make_move("U")
print("Actual BOARD", game3.board)