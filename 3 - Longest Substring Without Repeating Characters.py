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
        # Use 2 pointers to traverse the string, while using a hashmap to store character counts.

        hashmap = {}
        res = 0
        left = 0

        for r in range(len(s)):
            hashmap[s[r]] = hashmap.get(s[r], 0) + 1

            while hashmap[s[r]] > 1 and left < r:
                hashmap[s[left]] -= 1
                left += 1
            res = max(res, r - left + 1)

        return res

# Time Complexity: O(n) -> Single pass of array with 2 pointers.
# Space Complexity: O(m) -> Store up to every unique char in hashmap (represented by m).