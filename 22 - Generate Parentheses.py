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