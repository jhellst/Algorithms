# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false


# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Return True if anagram and False if not anagram.
        # Use a hashmap/counter.

        return collections.Counter(s) == collections.Counter(t)
å
# Time Complexity: O(s + t) -> Create a counter from both s and t.
# Space Complexity: O(s + t) -> Create a counter from both s and t.

# Note: We can use sorting to reduce memory, but with increased time complexity.