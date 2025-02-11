# You are given a string s.
# Your task is to remove all digits by doing this operation repeatedly:
#     Delete the first digit and the closest non-digit character to its left.
# Return the resulting string after removing all digits.

# Example 1:
# Input: s = "abc"
# Output: "abc"
# Explanation:
# There is no digit in the string.

# Example 2:
# Input: s = "cb34"
# Output: ""
# Explanation:
# First, we apply the operation on s[2], and s becomes "c4".
# Then we apply the operation on s[1], and s becomes "".

# Constraints:
#     1 <= s.length <= 100
#     s consists only of lowercase English letters and digits.
#     The input is generated such that it is possible to delete all digits.


class Solution:
    def clearDigits(self, s: str) -> str:
        # Step-by-step process.
        #   - Delete the 1st digit.
        #   - Delete the closest non-digit character to the left.


        answer = [] # Stack to hold chars.
        for char in s:
            if char in "0123456789" and answer:
                answer.pop()
            else:
                answer.append(char)

        return "".join(answer)

# Time Complexity: O(n) -> Visit each char once.
# Space Complexity: O(n) -> Store up to n chars on stack.