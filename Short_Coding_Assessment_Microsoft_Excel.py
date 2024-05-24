# Coding Assessment:
#   - Time Allotted: 65 Minutes after reading prompt
#   - Time Started: 3:10pm PT
#   - Time Stopped: 4:15pm PT

# Note: Got to working on print_computed in alloted time, but didn't finish.

# Link: https://docs.google.com/document/d/1mhiGPdePRzyv7U3vJ_TJ4JdKXy9-z1gNqHE-CfBCebc/edit

# Implement Microsoft Excel:
#   - "Spreadsheet App"
#       - Users can create spreadsheets
#       - Users can update a spreadsheet's cell with a string value.
#           -> user provides cell_index, string_input as inputs to update_cell()
#       - Cells support basic operations (+ - * /)
#       - Cells can be referenced
#       - Cells can contain double-quoted string values -> These are ignored during computations, but are included for final output.

#       - User can visualize ("print") a portion of the spreadsheet by providing the top left and bottom right indices.
#           - This prints the contained array, with every value in the array printed as a string.
#           - Methods:
#               -> print_computed(): prints the computed values of each cell
#                   -> This method will "eval" the contents of the cell with Python.
#               -> print_raw(): prints the string values of each cell, without evaluating.

# Important Questions:
#   - Do we care about being able to "look up" spreadsheets that we've created previously?
#   - How big is the default spreadsheet size? Or do spreadsheets have the ability to extend their range?


# OOP Implementation of Classes:


# class Spreadsheet:

#   Properties:
#   - self.cells = [[]] # 2D array that contains cells of the entire range.

#   Public Methods:
#   - update_cell(index, input_string)
#   - print_raw(top_left_index, bottom_right_index)
#   - print_computed(top_left_index, bottom_right_index)

#   Private Methods:
#   - _convert_coordinates(index) -> used to convert a reference like "A12" to [11, 0] -> (A is the first column and 12 is the 12th row.)
#   - _evaluate_cell(row_index, col_index) -> evaluates a cell completely.


# Final thoughts:
#   - Use a 2D array to store the "spreadsheet"
#   - Implement "print_raw" and "print_computed"
#       -> Key challenge here is to implement print_computed.
#           - We need to process operations in order -> a stack might work well for implementing.
#   - Column indices are a-z -> we'll need to use a conversion here to convert a letter to a

# Assumptions:
#   - Create sheets of Columns a-z and Rows 1-100.
#       - In a real-world implementation, this would be much larger to start and could be adjusted to add or remove rows/columns.
#   - For now, assuming that there are only columns A-Z AND the


class Spreadsheet:
    def __init__(self):
        row = [""] * 26  # Columns a-z for each row.
        self.sheet = [row[::] for _ in range(10)]  # 10 rows as default, for now.


    def _convert_coordinates(self, coordinates):
        """Given a coordinate consisting of a letter + a number, return a 2-indexed array for the corresponding row and column coordinates in the spreadsheet."""
        print("coordinates", coordinates)
        col_coord, row_coord = coordinates[0], coordinates[1:]
        print("col_coord", col_coord, "row_coord", row_coord)
        col_index = ord(col_coord) - ord("A")
        row_index = int(row_coord) - 1
        return [row_index, col_index]


    # Retrieve cell's raw contents -> evaluate the contents using a stack to maintain correct order of operations AND allow for other cells to be referenced.
    def _evaluate_elem(self, raw_contents):
        """Given a cell's string_contents, evaluates the cell's value based on all possible operations and references."""
        if raw_contents == "":
            return [""]
        print("raw_contents", raw_contents)
        operations_list = raw_contents.split(" ")
        print("operations_list", operations_list)

        stack = []

        for elem in operations_list:
            if elem.isnumeric(): # If elem is only a number.
                if stack and stack[-1] in "+-*/": # We have an operation to perform.
                    operation = stack.pop()
                    prev_num = stack.pop()
                    print("!", prev_num, operation)
                    stack.append(eval(str(prev_num[0]) + operation + elem))
                else:
                    stack.append(elem)

            elif elem in "+-*/": # If elem is a "sign" operation.
                stack.append(elem)

            elif elem[0] == "(": # Parentheses.
                stack.append(self._evaluate_elem(elem[1:len(elem) - 1]))

            elif elem[0].isalpha(): # If elem is a cell reference.
                r, c = self._convert_coordinates(elem)
                print(elem, r, c, self.sheet[r][c])
                stack.append(self._evaluate_elem(self.sheet[r][c]))

            elif elem[0] == "'": # Only text-based items, to be ignored in operations. Might need to revisit this.
                stack.append(elem)


        # Return the stack, but with all numbers re-converted into strings.
        return [str(elem) for elem in stack]



    def update_cell(self, index, input_string):
        """Updates the cell's value to be equal to the provided input string."""
        row, col = self._convert_coordinates(index)
        self.sheet[row][col] = input_string


    # Assuming that we want to print the entire array at once, rather than row-by-row.
    def print_raw(self, top_left_index, bottom_right_index):
        """Prints the raw contents of every cell in the specified range."""
        top_row, first_col = self._convert_coordinates(top_left_index)
        bottom_row, last_col = self._convert_coordinates(bottom_right_index)

        output_array = []

        for _row_index in range(top_row, bottom_row + 1):
            current_row = [self.sheet[_row_index][first_col: last_col+1]]
            output_array.append(current_row)

        # Print or return?
        print(output_array)


    # Important detail that cells can reference each other.
    def print_computed(self, top_left_index, bottom_right_index):
        """Prints the computed contents of every cell in the specified range."""
        top_row, first_col = self._convert_coordinates(top_left_index)
        bottom_row, last_col = self._convert_coordinates(bottom_right_index)

        output_array = []

        for _row_index in range(top_row, bottom_row + 1):
            for _col_index in range(first_col, last_col):
                raw_contents = self.sheet[_row_index][_col_index]
                print("raw_contents", raw_contents)

                output_array.append("".join(self._evaluate_elem(raw_contents)))

        # Print or return?
        print(output_array)



sheet = Spreadsheet()
print(sheet.sheet)
sheet.update_cell('B1', '6')
print(sheet.sheet)
sheet.update_cell('B2', 'B1 + 1')
print(sheet.sheet)
computed_values = sheet.print_raw('A1', 'C3')


# computed_values = sheet.print_computed('A1', 'C3')
# print("computed_values", computed_values)
