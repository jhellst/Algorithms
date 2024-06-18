from random import randrange
from collections import deque

# 2048 -> Algorithm to solve for

# Question Prompt:
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




# TODO: Add (or remove) logic to check for game_won and game_over.



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
        self.score = 2  # This will be the max value in the board at any point.
        self.game_over = False
        self.game_is_won = False

    def _check_if_loss(self):
        # Traverses game_board and looks for adjacent cells of equal value. If we find adjacent equal values OR an empty cell, return False immediately.
        #   - For each cell , we want to check the cell to the immediate right (if it exists) AND the cell immediately below (if it exists).
        """Checks if the player has lost the game. Returns True/False."""

        for row_index in range(0, 4):
            for col_index in range(0, 4):

                # If we find an empty space in the board, return False.
                if self.board[row_index][col_index] == 0:
                    return False

                # Check cell to immediate right, if we're not on the far right column of the board.
                if col_index < 3:
                    if self.board[row_index][col_index] == self.board[row_index][col_index + 1]:
                        return False

                # Check cell immediately below, if we're not on the bottom row of the board.
                if row_index < 3:
                    if self.board[row_index][col_index] == self.board[row_index + 1][col_index]:
                        return False

        # Return True if we've checked the entire board and cannot find any empty cells OR adjacent cells of equal value.
        return True

    def _insert_new_two(self):
        """Places a 2 in a randomly selected empty cell of the board."""
        new_two_placed = False
        while not new_two_placed:
            x, y = randrange(0, 4), randrange(0, 4)
            if self.board[x][y] == 0:
                self.board[x][y] = 2
                new_two_placed = True


    def make_move(self, direction):
        """Processes a single move made by the user. 'Slides' all values in that direction and combines any equal values that collide."""

        # Note: Logic will differ based on the direction. Each "move" will result in a shifting AND a combining step.
        # Tilt phone to the left -> all values slide to the left, but maintain the same row.
        # Then, combine horizontal cells of equal value, prioritizing combining any cells further to the left.

        # Construct each row's deque of values. Then, pop each value while checking to see if we can combine them.
        if direction == "R":
            for row_index in range(0, 4):
                cur_row_values = deque()

                for col_index in range(3, -1, -1):
                    cur_value = self.board[row_index][col_index]
                    self.board[row_index][col_index] = 0

                    if cur_value != 0:  # We have a number in this cell.
                        cur_row_values.append(cur_value)

                # Used to track the location where the next number will shift.
                insert_col_index = 3
                while cur_row_values:
                    val_to_insert = cur_row_values.popleft()
                    # If we have the same adjacent value -> combine.
                    if cur_row_values and cur_row_values[0] == val_to_insert: # Combination scenario.
                        cur_row_values.popleft()
                        val_to_insert *= 2
                    self.board[row_index][insert_col_index] = val_to_insert
                    insert_col_index -= 1

        elif direction == "L":
            for row_index in range(0, 4):
                cur_row_values = deque()

                for col_index in range(0, 4):
                    cur_value = self.board[row_index][col_index]
                    self.board[row_index][col_index] = 0

                    if cur_value != 0:
                        cur_row_values.append(cur_value)

                insert_col_index = 0
                while cur_row_values:
                    val_to_insert = cur_row_values.popleft()
                    # If we have the same adjacent value -> combine.
                    if cur_row_values and cur_row_values[0] == val_to_insert:
                        cur_row_values.popleft()
                        val_to_insert *= 2
                    self.board[row_index][insert_col_index] = val_to_insert
                    insert_col_index += 1

        elif direction == "U":
            for col_index in range(0, 4):
                cur_col_values = deque()

                for row_index in range(0, 4):
                    cur_value = self.board[row_index][col_index]
                    self.board[row_index][col_index] = 0

                    if cur_value != 0:
                        cur_col_values.append(cur_value)

                insert_row_index = 0
                while cur_col_values:
                    val_to_insert = cur_col_values.popleft()
                    # If we have the same adjacent value -> combine.
                    if cur_col_values and cur_col_values[0] == val_to_insert:
                        cur_col_values.popleft()
                        val_to_insert *= 2
                    self.board[insert_row_index][col_index] = val_to_insert
                    insert_row_index += 1

        elif direction == "D":
            for col_index in range(0, 4):
                cur_col_values = deque()

                for row_index in range(3, -1, -1):
                    cur_value = self.board[row_index][col_index]
                    self.board[row_index][col_index] = 0

                    if cur_value != 0:
                        cur_col_values.append(cur_value)

                insert_row_index = 3
                while cur_col_values:
                    val_to_insert = cur_col_values.popleft()
                    # If we have the same adjacent value -> combine.
                    if cur_col_values and cur_col_values[0] == val_to_insert:
                        cur_col_values.popleft()
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

        # Now, insert a 2 value in a randomly selected empty cell of the board.
        # self._insert_new_two()


# Possible Improvements:
#   - Not 100% necessary to store row/column values in a deque -> we could use pointers to prevent from using extra storage.
#       - In my opinion, because there are a maximum of 4 values per row/column, we don't have to worry too much about the cost/efficiency.
#   - We could use a dictionary that maps to the looping logic, so that we can avoid duplicating code between L, R, U, D in make_move().






# def game2048(grid, path):

# Example:
# grid = [[0, 0, 0, 0],
#         [0, 0, 2, 2],
#         [0, 0, 2, 4],
#         [2, 2, 4, 8]]

# path = "RR"


# game = Game2048(grid)
# print("Initial BOARD", game.board)
# game.make_move("R")
# print("ACUTAL BOARD", game.board)
# game.make_move("R")
# print("ACUTAL BOARD", game.board)

# print("EXAMPLE_BOARD", [[0, 0, 0, 0],
#                 [0, 0, 0, 4],
#                 [0, 0, 2, 4],
#                 [0, 0, 8, 8]])


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


# grid3 = [[2, 0, 0, 0], [2, 0, 0, 0], [4, 0, 0, 0], [0, 0, 0, 0]]
# game3 = Game2048(grid3)
# print("Initial BOARD", game3.board)
# game3.make_move("D")
# print("Actual BOARD", game3.board)
# game3.make_move("U")
# print("Actual BOARD", game3.board)


# grid4 = [[2, 4, 8, 16], [16, 32, 64, 128], [128, 256, 512, 1028], [1028, 2, 4, 8]]
# game4 = Game2048(grid4)
# print("Initial BOARD", game4.board)
# game4.make_move("D")
# print("Actual BOARD", game4.board)


# Tests:
# total_tests = 19

test_game_1 = Game2048([[0, 0, 0, 0],
                        [0, 0, 2, 2],
                        [0, 0, 2, 4],
                        [2, 2, 4, 8]])
test_game_1.make_move("R")
test_game_1.make_move("R")

print(test_game_1.board)
print([[0, 0, 0, 0],
       [0, 0, 0, 4],
       [0, 0, 2, 4],
       [0, 0, 8, 8]])
test_1 = (test_game_1.board ==
          [[0, 0, 0, 0],
           [0, 0, 0, 4],
              [0, 0, 2, 4],
              [0, 0, 8, 8]]
          )
print(test_1)


test_game_2 = Game2048([[0, 0, 0, 2],
                        [0, 0, 4, 2],
                        [0, 0, 4, 2],
                        [0, 0, 4, 2]])
test_game_2.make_move("D")

print(test_game_2.board)
print([[0, 0, 0, 0],
       [0, 0, 0, 4],
       [0, 0, 2, 4],
       [0, 0, 8, 8]])
test_2 = (test_game_2.board ==
          [[0, 0, 0, 0],
           [0, 0, 0, 0],
              [0, 0, 4, 4],
              [0, 0, 8, 4]]
          )
print(test_2)


test_game_3 = Game2048([[0, 2, 2, 0],
                        [0, 4, 2, 2],
                        [2, 4, 4, 8],
                        [2, 4, 0, 0]])
test_game_3.make_move("L")

print(test_game_3.board)
print([[4, 0, 0, 0],
       [4, 4, 0, 0],
       [2, 8, 8, 0],
       [2, 4, 0, 0]])
test_3 = (test_game_3.board ==
          [[4, 0, 0, 0],
           [4, 4, 0, 0],
              [2, 8, 8, 0],
              [2, 4, 0, 0]]
          )
print(test_3)


test_game_4 = Game2048([[0, 0, 0, 2],
                        [0, 0, 4, 2],
                        [0, 0, 4, 2],
                        [0, 0, 4, 2]])
test_game_4.make_move("D")
test_game_4.make_move("D")

print(test_game_4.board)
print([[0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 4, 0],
       [0, 0, 8, 8]])
test_4 = (test_game_4.board ==
          [[0, 0, 0, 0],
           [0, 0, 0, 0],
              [0, 0, 4, 0],
              [0, 0, 8, 8]]
          )
print(test_4)


test_game_5 = Game2048([[0, 0, 0, 2],
                        [0, 0, 4, 2],
                        [0, 0, 4, 2],
                        [0, 0, 4, 2]])
test_game_5.make_move("D")
test_game_5.make_move("R")
test_game_5.make_move("R")
test_game_5.make_move("D")

print(test_game_5.board)
print([[0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 8],
       [0, 0, 8, 4]])
test_5 = (test_game_5.board ==
          [[0, 0, 0, 0],
           [0, 0, 0, 0],
              [0, 0, 0, 8],
              [0, 0, 8, 4]]
          )
print(test_5)

test_game_6 = Game2048([[2, 4, 8, 16],
                        [256, 128, 64, 32],
                        [512, 1024, 2048, 4096],
                        [65536, 32768, 16384, 8192]])
test_game_6.make_move("U")
test_game_6.make_move("R")
test_game_6.make_move("L")
test_game_6.make_move("D")

print(test_game_6.board)
print([[2, 4, 8, 16],
       [256, 128, 64, 32],
       [512, 1024, 2048, 4096],
       [65536, 32768, 16384, 8192]])
test_6 = (test_game_6.board ==
          [[2, 4, 8, 16],
           [256, 128, 64, 32],
              [512, 1024, 2048, 4096],
              [65536, 32768, 16384, 8192]]
          )
print(test_6)


test_game_7 = Game2048([[0, 2, 0, 2],
                        [0, 4, 4, 2],
                        [0, 0, 4, 2],
                        [0, 0, 4, 2]])
test_game_7.make_move("L")
test_game_7.make_move("L")
test_game_7.make_move("U")

print(test_game_7.board)
print([[4, 4, 0, 0],
       [8, 2, 0, 0],
       [8, 0, 0, 0],
       [0, 0, 0, 0]])
test_7 = (test_game_7.board ==
          [[4, 4, 0, 0],
           [8, 2, 0, 0],
              [8, 0, 0, 0],
              [0, 0, 0, 0]]
          )
print(test_7)


test_game_8 = Game2048([[0, 2, 0, 2],
                        [0, 4, 4, 2],
                        [0, 0, 4, 2],
                        [0, 0, 4, 2]])
test_game_8.make_move("L")
test_game_8.make_move("L")
test_game_8.make_move("U")
test_game_8.make_move("R")

print(test_game_8.board)
print([[0, 0, 0, 8],
       [0, 0, 8, 2],
       [0, 0, 0, 8],
       [0, 0, 0, 0]])
test_8 = (test_game_8.board ==
          [[0, 0, 0, 8],
           [0, 0, 8, 2],
              [0, 0, 0, 8],
              [0, 0, 0, 0]]
          )
print(test_8)


test_game_9 = Game2048([[0, 0, 0, 2],
                        [0, 0, 4, 2],
                        [0, 0, 4, 2],
                        [0, 0, 4, 2]])
test_game_9.make_move("D")
test_game_9.make_move("R")
test_game_9.make_move("R")
test_game_9.make_move("L")

print(test_game_9.board)
print([[0, 0, 0, 0],
       [0, 0, 0, 0],
       [8, 0, 0, 0],
       [8, 4, 0, 0]])
test_9 = (test_game_9.board ==
          [[0, 0, 0, 0],
           [0, 0, 0, 0],
              [8, 0, 0, 0],
              [8, 4, 0, 0]]
          )
print(test_9)


test_game_10 = Game2048([[0, 0, 0, 2],
                         [0, 0, 4, 2],
                         [0, 0, 4, 2],
                         [0, 0, 4, 2]])
test_game_10.make_move("D")
test_game_10.make_move("R")
test_game_10.make_move("R")
test_game_10.make_move("L")
test_game_10.make_move("L")
test_game_10.make_move("D")


print(test_game_10.board)
print([[0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0],
       [16, 4, 0, 0]])
test_10 = (test_game_10.board ==
           [[0, 0, 0, 0],
            [0, 0, 0, 0],
               [0, 0, 0, 0],
               [16, 4, 0, 0]]
           )
print(test_10)


test_game_11 = Game2048([[0, 0, 0, 2],
                         [0, 0, 4, 2],
                         [0, 0, 4, 2],
                         [0, 0, 4, 2]])
test_game_11.make_move("D")
test_game_11.make_move("R")
test_game_11.make_move("R")
test_game_11.make_move("L")
test_game_11.make_move("L")
test_game_11.make_move("D")
test_game_11.make_move("U")
test_game_11.make_move("R")


print(test_game_11.board)
print([[0, 0, 16, 4],
       [0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0]])
test_11 = (test_game_11.board ==
           [[0, 0, 16, 4],
            [0, 0, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0]]
           )
print(test_11)


test_game_12 = Game2048([[0, 0, 0, 0],
                         [0, 0, 0, 0],
                         [0, 0, 0, 0],
                         [0, 0, 0, 0]])
test_game_12.make_move("D")
test_game_12.make_move("R")
test_game_12.make_move("R")
test_game_12.make_move("L")
test_game_12.make_move("L")
test_game_12.make_move("D")


print(test_game_12.board)
print([[0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0]])
test_12 = (test_game_12.board ==
           [[0, 0, 0, 0],
            [0, 0, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0]]
           )
print(test_12)


test_game_13 = Game2048([[0, 2, 0, 2],
                         [0, 4, 4, 2],
                         [0, 0, 4, 2],
                         [0, 0, 4, 2]])
test_game_13.make_move("L")

print(test_game_13.board)
print([[4, 0, 0, 0],
       [8, 2, 0, 0],
       [4, 2, 0, 0],
       [4, 2, 0, 0]])
test_13 = (test_game_13.board ==
                [[4, 0, 0, 0],
                 [8, 2, 0, 0],
                    [4, 2, 0, 0],
                    [4, 2, 0, 0]]
                )
print(test_13)


test_game_14 = Game2048([[0, 2, 0, 2],
                         [0, 4, 4, 2],
                         [0, 0, 4, 2],
                         [0, 0, 4, 2]])
test_game_14.make_move("L")
test_game_14.make_move("L")
test_game_14.make_move("U")
test_game_14.make_move("R")
test_game_14.make_move("L")
test_game_14.make_move("D")


print(test_game_14.board)
print([[0, 0, 0, 0],
       [0, 0, 0, 0],
       [8, 0, 0, 0],
       [16, 2, 0, 0]])
test_14 = (test_game_14.board ==
           [[0, 0, 0, 0],
            [0, 0, 0, 0],
            [8, 0, 0, 0],
            [16, 2, 0, 0]]
           )
print(test_14)


test_game_15 = Game2048([[0,0,0,2],
 [0,4,4,2],
 [0,4,4,2],
 [0,0,4,2]])
test_game_15.make_move("U")
test_game_15.make_move("R")
test_game_15.make_move("R")
test_game_15.make_move("R")

print(test_game_15.board)
print([[0,0,16,4],
 [0,0,0,8],
 [0,0,0,0],
 [0,0,0,0]])
test_15 = (test_game_15.board ==
           [[0,0,16,4],
 [0,0,0,8],
 [0,0,0,0],
 [0,0,0,0]]
           )
print(test_15)





test_game_16 = Game2048([[4,8,8,16],
 [0,0,2,2],
 [0,4,4,4],
 [16,32,0,0]])
test_game_16.make_move("L")

print(test_game_16.board)
print([[4,16,16,0],
 [4,0,0,0],
 [8,4,0,0],
 [16,32,0,0]])
test_16 = (test_game_16.board ==
           [[4,16,16,0],
 [4,0,0,0],
 [8,4,0,0],
 [16,32,0,0]]
           )
print(test_16)





test_game_17 = Game2048([[2,2,2,2],
 [2,2,2,2],
 [2,2,2,2],
 [2,2,2,2]])
test_game_17.make_move("R")
test_game_17.make_move("R")
test_game_17.make_move("U")
test_game_17.make_move("U")
test_game_17.make_move("D")


print(test_game_17.board)
print([[0,0,0,0],
 [0,0,0,0],
 [0,0,0,0],
 [0,0,0,32]])
test_17 = (test_game_17.board ==
           [[0,0,0,0],
 [0,0,0,0],
 [0,0,0,0],
 [0,0,0,32]]
           )
print(test_17)





test_game_18 = Game2048([[2,2,4,8],
 [128,64,32,16],
 [256,512,1024,2048],
 [32768,16384,8192,4096]])
# path: "RRRDLLLDRRRDLLL"
test_game_18.make_move("R")
test_game_18.make_move("R")
test_game_18.make_move("R")
test_game_18.make_move("D")
test_game_18.make_move("L")
test_game_18.make_move("L")
test_game_18.make_move("L")
test_game_18.make_move("D")
test_game_18.make_move("R")
test_game_18.make_move("R")
test_game_18.make_move("R")
test_game_18.make_move("R")
test_game_18.make_move("D")
test_game_18.make_move("L")
test_game_18.make_move("L")
test_game_18.make_move("L")


print(test_game_18.board)
print([[0,0,0,0],
 [0,0,0,0],
 [0,0,0,0],
 [65536,0,0,0]])
test_18 = (test_game_18.board ==
           [[0,0,0,0],
 [0,0,0,0],
 [0,0,0,0],
 [65536,0,0,0]]
           )
print(test_18)





test_game_19 = Game2048([[2,4,8,2],
 [0,0,0,0],
 [0,0,0,0],
 [65536,0,0,0]])
# path: "RRRRRRRRRRRRRRRRLLLLLLLLLLLUUU"
test_game_19.make_move("R")
test_game_19.make_move("R")
test_game_19.make_move("R")
test_game_19.make_move("R")
test_game_19.make_move("R")
test_game_19.make_move("R")
test_game_19.make_move("R")
test_game_19.make_move("R")
test_game_19.make_move("R")
test_game_19.make_move("R")
test_game_19.make_move("R")
test_game_19.make_move("R")
test_game_19.make_move("R")
test_game_19.make_move("R")
test_game_19.make_move("R")
test_game_19.make_move("R")
test_game_19.make_move("L")
test_game_19.make_move("L")
test_game_19.make_move("L")
test_game_19.make_move("L")
test_game_19.make_move("L")
test_game_19.make_move("L")
test_game_19.make_move("L")
test_game_19.make_move("L")
test_game_19.make_move("L")
test_game_19.make_move("L")
test_game_19.make_move("L")
test_game_19.make_move("U")
test_game_19.make_move("U")
test_game_19.make_move("U")

print(test_game_19.board)
print([[2,4,8,2],
 [65536,0,0,0],
 [0,0,0,0],
 [0,0,0,0]])
test_19 = (test_game_19.board ==
           [[2,4,8,2],
 [65536,0,0,0],
 [0,0,0,0],
 [0,0,0,0]]
           )
print(test_19)



tests_passed = sum([test for test in [test_1, test_2, test_3,
                   test_4, test_5, test_6, test_7, test_8, test_9, test_10, test_11, test_12, test_13, test_14, test_15, test_16, test_17, test_18, test_19]])
print("Tests Passed: ", tests_passed, "out of 19")