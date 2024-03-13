# You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.
# Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.
# Return a list of integers representing the size of these parts.

# Example 1:

# Input: s = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.

# Example 2:

# Input: s = "eccbbbbdec"
# Output: [10]

# Constraints:

# 1 <= s.length <= 500
# s consists of lowercase English letters.


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # We want to traverse the array and separate it into partitions.
        # Each letter can only be contained in 1 partition.
        # Key takeaway: Each partition's size is limited by the existence of other same chars later in the string.

        res = []

        # Make a hashMap for positions and letters.
        letterCounts = collections.Counter(s)

        # Key takeaway: Once we see a letter, we MUST include every occurence of that character in the current partition.
        #   - Every new letter we see, we MUST reset the partition's end point.
        # End the partition if we don't need to continue (if we are at the pre-determined endpoint).
        # As we traverse, reduce the letterCount by 1 as you pass a letter.

        letterPositions = {}
        for i, char in enumerate(s):
            letterPositions[char] = i

        start = 0 # Point that partition will end at. (Starts at 0, but will reset each time a partition ends).
        end = 0 # Point that partition will end at. (Starts at 1, but will be reset if first char is not unique in string).

        for i, char in enumerate(s):

            if letterCounts.get(char, 0) == 1: # Last of this char.
                letterCounts[char] -= 1
                # Now, check if we are are pre-determined end point. If so, partition. Otherwise, continue.
                if i >= end:
                    res.append(end - start + 1)
                    start = end + 1
                    end = start
            else: # Not last of this char. Reset end to be max(end, lastCharPosition).
                letterCounts[char] -= 1
                end = max(end, letterPositions[char])

        return res

# Time Complexity: O(n) -> Traverse the string twice, also must create the counter.
# Space Complexity: O(1) -> Store up to 26 chars in data structure.