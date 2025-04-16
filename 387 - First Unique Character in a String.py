# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

# Example 1:
# Input: s = "leetcode"
# Output: 0
# Explanation:
# The character 'l' at index 0 is the first character that does not occur at any other index.

# Example 2:
# Input: s = "loveleetcode"
# Output: 2

# Example 3:
# Input: s = "aabb"
# Output: -1

# Constraints:
#     1 <= s.length <= 105
#     s consists of only lowercase English letters.



class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Create a counter, then traverse the characters in s -> if count == 1, return its index immediately.

        c = Counter(s)
        for i, char in enumerate(s):
            count = c[char]
            if count == 1:
                return i

        return -1

# Time Complexity: O(n) -> Create a counter from string of length n, then traverse string of length n.
# Space Complexity: O(n) -> In worst case, counter will contain n keys.