# Given a string s, return the longest palindromic substring in s.

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.

# Example 2:

# Input: s = "cbbd"
# Output: "bb"

# Constraints:

# 1 <= s.length <= 1000
# s consist of only digits and English letters.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Want to find and return the longest palindrome.
        # To check if palindrome, we

        # Use a pointer to traverse the string. At each point, extend the palindrome outward and check if it is a palindrome still.
        # Note: We need to separately check odd and even length palindromes.

        res = ""
        resLen = 0

        # Odd-length palindrome check
        for i in range(len(s)):
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > resLen:
                    res = s[left:right + 1]
                    resLen = right - left + 1
                left -= 1
                right += 1

        # Even-length palindrome check
        for i in range(len(s) - 1):
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > resLen:
                    res = s[left:right + 1]
                    resLen = right - left + 1
                left -= 1
                right += 1

        return res

# Time Complexity: O(n^2) -> Loop through each index, then expand outward (potentially to entire string).
# Space ComplexityL O(1) -> No additional storage needed.