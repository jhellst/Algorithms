# You are given a string s of lowercase English letters and an integer array shifts of the same length.
# Call the shift() of a letter, the next letter in the alphabet, (wrapping around so that 'z' becomes 'a').

# For example, shift('a') = 'b', shift('t') = 'u', and shift('z') = 'a'.
# Now for each shifts[i] = x, we want to shift the first i + 1 letters of s, x times.

# Return the final string after all such shifts to s are applied.



# Example 1:

# Input: s = "abc", shifts = [3,5,9]
# Output: "rpl"
# Explanation: We start with "abc".
# After shifting the first 1 letters of s by 3, we have "dbc".
# After shifting the first 2 letters of s by 5, we have "igc".
# After shifting the first 3 letters of s by 9, we have "rpl", the answer.
# Example 2:

# Input: s = "aaa", shifts = [1,2,3]
# Output: "gfd"


# Constraints:

# 1 <= s.length <= 105
# s consists of lowercase English letters.
# shifts.length == s.length
# 0 <= shifts[i] <= 109



class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:

        # For each successive "shift", we would like to shift all characters at or before the current index.
        # Therefore, for a string with length of 3 we will shift index 0 in 3 separate operations.
        # All letters are lowercase, so we are working from ord between 97 and 122.
        # The shift must be simplified by modding it with 26, so that it "wraps around" if there is a greater shift than length of letters. We can achieve this by first adding all of the shifts, then modding the indices.

        # Trick to improve time complexity: Use a prefix sum to calculate total sum of shifts for index 0, then at each successive index, subtract the value of index i - 1.

        shiftSum = sum(shifts)
        res = ""

        for i, char in enumerate(s):
            charIndex = ord(char) - 97 # ord of character, adjusted to make a -> 0

            newCharIndex = (charIndex + shiftSum) % 26
            newChar = chr(newCharIndex + 97)

            shiftSum -= shifts[i]
            res += newChar

        return res

# Time Complexity: 2 * O(n) -> O(n) -> We sum the array of shifts once, and we traverse the array once while transforming.