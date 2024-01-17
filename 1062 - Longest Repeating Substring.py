# Given a string s, return the length of the longest repeating substrings. If no repeating substring exists, return 0.

# Example 1:

# Input: s = "abcd"
# Output: 0
# Explanation: There is no repeating substring.
# Example 2:

# Input: s = "abbaba"
# Output: 2
# Explanation: The longest repeating substrings are "ab" and "ba", each of which occurs twice.
# Example 3:

# Input: s = "aabcaabdaab"
# Output: 3
# Explanation: The longest repeating substring is "aab", which occurs 3 times.


# Constraints:

# 1 <= s.length <= 2000
# s consists of lowercase English letters.


class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:

        # Add all substrings into hash table. As you do this, increase the value of res every time you put a longer repeating substring.
        res = 0
        hashMap = {}

        for i in range(len(s)):
            for j in range(i, len(s)):
                curSubstring = s[i:j+1]
                count = hashMap.get(curSubstring, 0)
                newCount = count + 1
                hashMap[curSubstring] = newCount

                if newCount > 1 and len(curSubstring) > res:
                    res = len(curSubstring)

        return res


# Time Complexity: O(n^2)