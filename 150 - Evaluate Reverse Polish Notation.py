# You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

# Evaluate the expression. Return an integer that represents the value of the expression.

# Note that:

# The valid operators are '+', '-', '*', and '/'.
# Each operand may be an integer or another expression.
# The division between two integers always truncates toward zero.
# There will not be any division by zero.
# The input represents a valid arithmetic expression in a reverse polish notation.
# The answer and all the intermediate calculations can be represented in a 32-bit integer.

# Example 1:

# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9

# Example 2:

# Input: tokens = ["4","13","5","/","+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6

# Example 3:

# Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# Output: 22
# Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22

# Constraints:

# 1 <= tokens.length <= 104
# tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].


class Solution:
    def evalRPN(self, tokens: 'list[str]') -> int:
        # Use a stack to store number values. When we see a sign, take the top 2 numbers on the stack and run the operation.

        stack = []
        for token in tokens:
            if token in {"+", "-", "*", "/"}: # Token is a sign.
                num2 = stack.pop()
                num1 = stack.pop() # Note, num1 will come first in the operation evaluation.
                if token == "+":
                    curNum = num1 + num2
                elif token == "-":
                    curNum = num1 - num2
                elif token == "*":
                    curNum = num1 * num2
                else:
                    curNum = num1 / num2
                    if curNum > 0: # Truncate toward 0.
                        curNum = math.floor(curNum)
                    else:
                        curNum = math.ceil(curNum)
                stack.append(curNum)
            else: # Token is a num.
                stack.append(int(token)) # Add number to stack.

        return stack[-1]

# Time Complexity: O(n) -> Single pass of tokens array.
# Space Complexity: O(n) -> Store on stack up to every number in the array.