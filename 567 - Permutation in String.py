# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
# In other words, return true if one of s1's permutations is the substring of s2.

# Example 1:

# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").

# Example 2:

# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false

# Constraints:

# 1 <= s1.length, s2.length <= 104
# s1 and s2 consist of lowercase English letters.


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # 2-pointers / Sliding-window solution. We want to construct the curDict of chars that are including in the substring. Compare this with s1.

        if len(s1) > len(s2):
            return False
        elif s1 == s2:
            return True

        curDict = {} # Dict to hold
        c = collections.Counter(s1) # Dict to match with for a TRUE response.
        left, right = 0, 0

        for i in range(len(s1)):
            curDict[s2[i]] = curDict.get(s2[i], 0) + 1
            right += 1

        if curDict == c:
            return True

        # Now, traverse the grid with the sliding window at a fixed length.

        while right < len(s2):
            curDict[s2[left]] = curDict.get(s2[left], 0) - 1
            curDict[s2[right]] = curDict.get(s2[right], 0) + 1
            if curDict.get(s2[left], 0) == 0:
                del curDict[s2[left]]
            left += 1
            right += 1
            if curDict == c:
                return True

        return False

# Time Complexity: O(n) -> Single pass of each element in array, exactly 2 times.
# Space Complexity: O(n) -> Store each char in s1 up to once in dict. 2nd dict to also store all chars in s2.