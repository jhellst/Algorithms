# Given a string s, find the length of the longest substring without repeating characters.


# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


# Constraints:

# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Sliding-window style problem.
        # We want to start at index 0, expanding the window until we hit a repeating character. Shrink window from left in that case.
        # Use a set to store characters in the current substring.

        left = 0
        right = 0
        chars = set()
        res = 0

        # Here, we want to slide the window wider as long as we can. If we can't, reduce from the left side.
        while right < len(s):
            if s[right] in chars: # Here we have s[right] in the substring. Reduce from the left.
                chars.remove(s[left])
                left += 1
            else:
                res = max(res, right - left + 1)
                chars.add(s[right])
                right += 1

        return res


# Time Complexity: Single Pass -> O(n)
# Space Complexity: Worst case -> store every value in set one time -> O(n)