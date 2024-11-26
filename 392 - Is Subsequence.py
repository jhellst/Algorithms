# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

# Example 1:
# Input: s = "abc", t = "ahbgdc"
# Output: true

# Example 2:
# Input: s = "axc", t = "ahbgdc"
# Output: false

# Constraints:
#     0 <= s.length <= 100
#     0 <= t.length <= 104
#     s and t consist only of lowercase English letters.

# Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?



class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Return True if s can be found, in-order, within t. Return False otherwise.
        # Traverse s while maintaining a pointer for t_index (or vice-versa).
        #   - Basically, we want to increment the pointer as we check for the needed letters.
        # Counter isn't 100% needed -> we can just traverse each string with pointers while comparing.
        # One possible optimization would be to check counter initially to determine if we have the chars to form a subsequence.

        needed_chars = Counter(s)
        s_index = 0

        for char in t:
            if not needed_chars:
                return True
            if s_index >= len(s):
                return False
            if char in needed_chars and s_index < len(s) and s[s_index] == char:
                needed_chars[char] -= 1
                s_index += 1
                if needed_chars[char] == 0:
                    del needed_chars[char]

        return not needed_chars

# Time Complexity: O(2s + t) -> Create counter from s, then traverse both t and s one time (in worst case).
# Space Complexity: O(s) -> Store s chars in counter.