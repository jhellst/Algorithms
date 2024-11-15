# Given an integer x, return true if x is a palindrome , and false otherwise.

# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.

# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

# Example 3:

# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

# Constraints:
#     -231 <= x <= 231 - 1

# Follow up: Could you solve it without converting the integer to a string?



class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Return True if number is a palindrome, False if not.
        #   - If number is negative, it can never be a palindrome.
        #   - We can convert the number to a string to compare it vs. itself reversed.

        if x < 0:
            return False

        num_string = str(x)
        return num_string == num_string[::-1]

# Time Complexity: O(n) -> Reverse string of length n.
# Space Complexity: O(1) -> No additional storage used.