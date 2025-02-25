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



# 2nd Solution:

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Group the anagrams together in lists within res.
        # Use a dict -> key: value -> char_counter:[word1, word2, ...]
        # Note: No need to use a dict -> we can simply sort the numbers and use that value as the key.

        res = []
        d = {}

        for word in strs:
            sorted_word = "".join(sorted(word))

            if sorted_word in d:
                d[sorted_word].append(word)
            else:
                d[sorted_word] = [word]

        for key in d:
            res.append(d[key])

        return res

# Time Complexity: O(n * k * log(k)) -> Visit every word in strs array and sort/store in dict, then iterate through each key in d and append to res.
# Space Complexity: O(n) -> Store n words in dictionary.



# 3rd Solution:

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Group the anagrams of each word in strs.
        #   - Anagrams have the same letters (and count of letters) in any order.

        # First, create a hashmap with key:value represented by sorted_str:[str1, str2, ...]

        hashmap = {} # sorted_str: [str1, str2, ...]
        for string in strs:
            sorted_str = "".join(sorted(string))
            if sorted_str in hashmap:
                hashmap[sorted_str].append(string)
            else:
                hashmap[sorted_str] = [string]


        res = []
        for key, val in hashmap.items():
            res.append(val)

        return res

# Time Complexity: O(n * klog(k)) -> Loop through each string and sort/store in hashmap.
# Space Complexity: O(n) -> Store up to n words in hashmap.