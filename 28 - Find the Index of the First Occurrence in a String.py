# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# Example 1:

# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.

# Example 2:

# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.

# Constraints:
#     1 <= haystack.length, needle.length <= 104
#     haystack and needle consist of only lowercase English characters.



class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Find the needle and return the index. If not present, return -1.
        # Sliding window solution.

        left, right = 0, len(needle) - 1

        while right < len(haystack):
            if haystack[left:right+1] == needle:
                return left
            left += 1
            right += 1

        return -1

# Time Complexity: O(n * m) -> Single pass of haystack, taking a slice of len(m) of haystack at each window location.
# Space Complexity: O(1) -> No additional storage used.