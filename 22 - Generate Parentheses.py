# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]

# Example 2:

# Input: n = 1
# Output: ["()"]

# Constraints:

# 1 <= n <= 8


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Backtracking. Keep track of counts of open and closed parens.

        # stack = []
        res = []

        def backtrack(openCount, closedCount, stack):
            if openCount == closedCount == n: # We have used all parens.
                res.append("".join(stack))
                return

            if openCount < n: # Open paren is an option.
                stack.append("(")
                backtrack(openCount + 1, closedCount, stack)
                stack.pop()
            if closedCount < openCount:
                stack.append(")")
                backtrack(openCount, closedCount + 1, stack)
                stack.pop()


        backtrack(0, 0, [])
        return res


# Time Complexity: O(4^n / sqrt(n))
# Space Complexity: O(n) -> Stack may contain up to n calls at a time.



# 2nd Solution:

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Use a stack, pop and append to simulate different combos.
        # Each group of parens "()" must be nested or sequential
        #   - Must start with open paren AND we can't ever have more closed than open on the stack.

        res = []

        def recurse(num_open, num_closed, stack):
            if num_open == num_closed == n:
                res.append("".join(stack))
                return
            if num_open < n:
                stack.append("(")
                recurse(num_open + 1, num_closed, stack)
                stack.pop()
            if num_closed < num_open:
                stack.append(")")
                recurse(num_open, num_closed + 1, stack)
                stack.pop()
            return

        res = []

        recurse(0, 0, [])
        return res

# Time Complexity: O(n^2) -> O(4^n / n*sqrt(n))
# Space Complexity: O(n) -> Recursive calls stored on stack -> Maximum stack size will be 2*n.