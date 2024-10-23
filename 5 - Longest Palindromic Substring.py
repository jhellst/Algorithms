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


# 2nd Solution:

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Find the longest palindromic substring within s.
        # DP-style solution. At each index, we'll store the max_substring_length (and the max_substring).
        #   - Need to check for palindromes in strings of 1) even-length and 2) odd-length.

        res, res_len = "", 0

        # Odd-length -> check x units from i.
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]: # Continue expanding as long as it remains a palindrome.
                if (r - l + 1) >= res_len:
                    res = s[l:r+1]
                    res_len = r - l + 1
                l -= 1
                r += 1

        # Even-length -> check 2 center units.
        for i in range(len(s) - 1):
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]: # Continue expanding as long as it remains a palindrome.
                if (r - l + 1) >= res_len:
                    res = s[l:r+1]
                    res_len = r - l + 1
                l -= 1
                r += 1

        return res

# Time Complexity: O(n) -> Visit every index of x up to 2 times.
# Space Complexity: O(1) -> No additional storage used.