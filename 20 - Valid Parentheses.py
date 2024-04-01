# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.


# Example 1:

# Input: s = "()"
# Output: true

# Example 2:

# Input: s = "()[]{}"
# Output: true

# Example 3:

# Input: s = "(]"
# Output: false

# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.


class Solution:
    def isValid(self, s: str) -> bool:
        # Determine if the parentheses close each other properly. Stack-style solution.
        # If [, {, or ( -> Open, want to add this to the stack.
        # If ), }, or ] -> Closed, need to pop from the stack. If not matching, return False.

        parens = {")": "(", "]": "[", "}": "{",} # Matches closing to opening parentheses.
        stack = []

        for char in s:
            if char in parens: # If found, it is a closing parentheses.
                if not stack: # Stack doesn't contain any opening parens, so can't have a closing paren.
                    return False
                if stack[-1] != parens[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)

        return len(stack) == 0


# Time Complexity: O(n) -> Traverse string, visiting each char once.
# Space Complexity: O(n) -> Store up to every character on the stack.