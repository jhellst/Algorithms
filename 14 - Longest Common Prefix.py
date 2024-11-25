# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

# Constraints:
#     1 <= strs.length <= 200
#     0 <= strs[i].length <= 200
#     strs[i] consists of only lowercase English letters.



class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Continue to expand the cur_index as long as all characters in strs match at that index.

        for char_index in range(len(strs[0])):
            check_char = strs[0][char_index]
            for word in strs[1:]:
                if char_index >= len(word) or word[char_index] != check_char: # Chars don't match (or word isn't long enough), previous length is maximum matching length.
                    return strs[0][:char_index]
        return strs[0]

# Time Complexity: O(n * w) -> In worst case, we iterate through every char of every word in strs.
# Space Complexity: O(1) -> No additional storage used.