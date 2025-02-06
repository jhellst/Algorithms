# You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose two indices in a string (not necessarily different) and swap the characters at these indices.
# Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings. Otherwise, return false.

# Example 1:
# Input: s1 = "bank", s2 = "kanb"
# Output: true
# Explanation: For example, swap the first character with the last character of s2 to make "bank".

# Example 2:
# Input: s1 = "attack", s2 = "defend"
# Output: false
# Explanation: It is impossible to make them equal with one string swap.

# Example 3:
# Input: s1 = "kelb", s2 = "kelb"
# Output: true
# Explanation: The two strings are already equal, so no string swap operation is required.

# Constraints:
#     1 <= s1.length, s2.length <= 100
#     s1.length == s2.length
#     s1 and s2 consist of only lowercase English letters.



class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        # We can "swap" 2 characters exactly once.
        #   - Key Takeaway: If there is exactly 0 OR 2 chars out of place, we can return True.
        #       -> This is because we need to do 1 OR 0 swaps to have a valid swap, per the problem description.
        #   - Also: Must check that the "swap" characters are available. We can't just NEED 2 swaps, we must NEED 2 swaps that involve the same chars.

        if Counter(s1) != Counter(s2): # Need to confirm that each string has the same character counts -> we can sort the strings, or use a counter.
            return False

        wrong_char_count = 0

        for i, char_s1 in enumerate(s1):
            char_s2 = s2[i]
            if char_s1 != char_s2: # Swap needed
                wrong_char_count += 1

        return wrong_char_count in (0, 2)

# Time Complexity: O(n) -> Create counters from s1 and s2, then visit each char in s1 (and s2) one time.
# Space Complexity: O(1) -> No additional storage used.