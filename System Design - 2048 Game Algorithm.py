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
#   1) Iterate through all of the "directions" provided in path.
#   2)

def solution(grid, path):
    for direction in path:
        switcher = {
            'L': (0, -1),
            'R': (0, 1),
            'D': (1, 0),
            'U': (-1, 0)
        }
        dx, dy = switcher.get(direction)

        start = [[0] * 2 for i in range(4)]
        if direction == 'L' or direction == 'R':
            for j in range(4):
                start[j][0] = j
                start[j][1] = 3 if dy > 0 else 0
        else:
            for j in range(4):
                start[j][0] = 3 if dx > 0 else 0
                start[j][1] = j
        for j in range(4):
            boundX = start[j][0] + dx
            boundY = start[j][1] + dy
            for k in range(4):
                posX = start[j][0]
                posY = start[j][1]
                # print((posX, posY))
                value = grid[posX][posY]
                if value != 0:
                    grid[posX][posY] = 0
                    while ((posX + dx != boundX or posY + dy != boundY)
                            and grid[posX + dx][posY + dy] == 0):
                        posX += dx
                        posY += dy
                    if ((posX + dx != boundX or posY + dy != boundY)
                        and grid[posX + dx][posY + dy] == value):
                        grid[posX + dx][posY + dy] += value
                        boundX = posX + dx
                        boundY = posY + dy
                    else:
                        grid[posX][posY] = value
                start[j][0] -= dx
                start[j][1] -= dy
    return grid


# Example:

grid = [[0, 0, 0, 0],
        [0, 0, 2, 2],
        [0, 0, 2, 4],
        [2, 2, 4, 8]]

path = "RR"

# print(solution(grid, path))

# solution(grid, path) = [[0, 0, 0, 0],
#                         [0, 0, 0, 4],
#                         [0, 0, 2, 4],
#                         [0, 0, 8, 8]]