# Given a string s, return the number of palindromic substrings in it.
# A string is a palindrome when it reads the same backward as forward.
# A substring is a contiguous sequence of characters within the string.

# Example 1:

# Input: s = "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".

# Example 2:

# Input: s = "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

# Constraints:

#     1 <= s.length <= 1000
#     s consists of lowercase English letters.


class Solution:
    def countSubstrings(self, s: str) -> int:
        # Count every palindromic substring contained within the string.
        # Need to check for palindromes of 1) odd-length and 2) even-length

        count = 0

        # Odd-length.
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1

        # Even-length.
        for i in range(len(s) - 1):
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1

        return count

# Time Complexity: O(n^2) -> Double-nested loop through each index of s.
# Space Complexity: O(1) -> No additional storage used.