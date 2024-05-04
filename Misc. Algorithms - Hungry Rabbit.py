import math

# A very hungry rabbit is placed in the center of a garden represented by a rectangular N x M 2D matrix.
# The values of the matrix will represent numbers of carrots available to the rabbit in each square of the garden.
# If the garden does not have an exact center, the rabbit should start in the square closest to the center with the highest carrot count.
# On a given turn, the rabbit will eat the carrots available on the square that it is on, then move up, down, left or right, choosing the square
# that has the most carrots. If there are no carrots left on any of the adjacent squares, the rabbit will go to sleep.
# You may assume that the rabbit will never have to choose between two squares with the same number of carrots.

# Write a function which takes a garden matrix and returns the number of carrots the rabbit eats.
# You may assume the matrix is rectangular with at least 1 row and 1 column, and that it is populated with non-negative integers.

arr = [[1, 2, 3, 4, 5],
       [6, 7, 8, 9, 10],
       [11, 12, 13, 14, 15],
       [1, 2, 3, 4, 5]]

arr2 = [[1, 2, 3, 4, 5],
       [6, 7, 8, 9, 10],
       [11, 12, 13, 14, 15],
       [1, 2, 3, 4, 5],
       [6, 7, 8, 9, 10]]

arr3 = [[1, 2, 3, 4, 5, 16],
       [6, 7, 8, 9, 10, 17],
       [11, 12, 13, 14, 15, 18],
       [1, 2, 3, 4, 5, 19],
       [6, 7, 8, 9, 10, 20]]

arr4 = [[1, 3, 501, 7],
        [10, 30, 50, 70],
        [100, 300, 500, 700]]


def hungry_rabbit(garden): # A rabbit starts at exactly the center (if it exists). Then, it will greddily move to the adjacent square with the most carrots and eat them all.
    numRows, numCols = len(garden), len(garden[0])

    # Now, determine (for both rows and cols) if there are 1 or 2 rows/cols to check. Max # of cells will be 4. We can have 1, 2, or 4.
    startingRows = []
    if numRows % 2 == 0: # Even number of rows, therefore we need 2.
        startingRows.append(math.ceil(numRows / 2) - 1)
        startingRows.append(math.ceil(numRows / 2))
    else:
        startingRows.append(math.ceil(numRows / 2) - 1)

    startingCols = []
    if numCols % 2 == 0: # Even number of rows, therefore we need 2.
        startingCols.append(math.ceil(numCols / 2) - 1)
        startingCols.append(math.ceil(numCols / 2))
    else:
        startingCols.append(math.ceil(numCols / 2) - 1)

    # Now, iterate through all possible starting cells. Starting indices will be at the max value.
    maxVal = None
    maxRow, maxCol = None, None
    for row in startingRows:
        for col in startingCols:
            if not maxVal or maxVal <= garden[row][col]:
                maxVal = garden[row][col]
                maxRow, maxCol = row, col

    # Now, we have the starting indices for our traversal. Start to traverse, selecting the highest adjacent value. Keep track of values we visit by setting them to -1.
    # print("maxRow", maxRow, "maxCol", maxCol)

    carrots_eaten = 0

    curRow, curCol = maxRow, maxCol # Starting index, we'll traverse to edge now. Terminate once we're at the edge (or just stepped off of the edge).

    while 0 < curRow < numRows - 1 and 0 < curCol < numCols - 1:
        carrots_eaten += garden[curRow][curCol] # Eat the carrots at the current cell.
        garden[curRow][curCol] = -1
        # Check values in all directions. Add the max value and step to that index.
        maxNextVal = None
        nextR, nextC = None, None
        for r, c in [[curRow + 1, curCol], [curRow - 1, curCol], [curRow, curCol + 1], [curRow, curCol - 1]]:
            if not maxNextVal or maxNextVal <= garden[r][c]:
                maxNextVal = garden[r][c]
                nextR, nextC = r, c
        # Now, we know which direction we'll step in.
        if not maxNextVal:
            break
        curRow, curCol = nextR, nextC

    # Add final cell value.
    carrots_eaten += garden[curRow][curCol]

    return carrots_eaten





print(hungry_rabbit(arr))
print(hungry_rabbit(arr2))
print(hungry_rabbit(arr3))
print(hungry_rabbit(arr4))