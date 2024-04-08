# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Example 2:

# Input: strs = [""]
# Output: [[""]]

# Example 3:

# Input: strs = ["a"]
# Output: [["a"]]

# Constraints:

# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        d = {}
        for string in strs:
            sortedString = "".join(sorted(string))

            if sortedString in d:
                d[sortedString].append(string)
            else:
                d[sortedString] = [string]

        res = [d[key] for key in d]
        return res

# Time Complexity: O(nk * log(k)) -> Traverse each s in strs, and sort each string/store in dict. n = len(strs) and k = max word length.
# Space Complexity: O(nk) -> Store every string in hashmap.