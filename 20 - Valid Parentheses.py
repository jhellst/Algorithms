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




# 2nd Solution:

class Solution:
    def isValid(self, s: str) -> bool:
        # We can only construct nested brackets in certain cases.
        #   - We can't ever have more closed parens (at any point as we traverse left -> right).
        #   - We have to "close" every paren -> open_count == closed_count
        # Use a stack to store the "nesting" of the parens, then process the string s.
        #   - Pop from the stack when a paren is "closed".
        #   - In the end, return True if open_count == closed_count AND the stack is empty.

        open_count, closed_count = 0, 0
        parens = {")": "(", "]": "[", "}": "{"} # Matches closing to opening parentheses.

        stack = []
        for char in s:
            if char in parens: # If char is a closed paren.
                if open_count == closed_count:
                    return False
                if stack and stack[-1] == parens[char]:
                    stack.pop()

                closed_count += 1
            else: # Char is an open paren.
                open_count += 1
                stack.append(char)

        if not stack:
            return True
        return False

# Time Complexity: O(n) -> Visit each char in s one time.
# Space Complexity: O(n) -> Store up to n items on a stack.