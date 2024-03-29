# The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

# For example, "ACGAATTCCG" is a DNA sequence.
# When studying DNA, it is useful to identify repeated sequences within the DNA.

# Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.

# Example 1:

# Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# Output: ["AAAAACCCCC","CCCCCAAAAA"]

# Example 2:

# Input: s = "AAAAAAAAAAAAA"
# Output: ["AAAAAAAAAA"]

# Constraints:

# 1 <= s.length <= 105
# s[i] is either 'A', 'C', 'G', or 'T'.


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        # Use a set to store each 10-char sequence as you traverse. If the same sequence was seen before, add it to res.

        seen = set()
        res = set()

        for i in range(len(s) - 9): # Traverse the range of all possible 10-character sequences.
            curSequence = s[i:i+10]

            if curSequence in seen:
                res.add(curSequence)
            else:
                seen.add(curSequence)

        return res

# Time Complexity: O(n) -> Single pass of string.
# Space Complexity: O(n - 9) -> O(n) -> Store every valid sequence, which is len(nums) - 9.