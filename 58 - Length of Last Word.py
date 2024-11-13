# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal
# substring
#  consisting of non-space characters only.

# Example 1:

# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.

# Example 2:

# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.

# Example 3:

# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Traverse s, char by char -> keeping track of length. When you reach a space, reset length to 0.
        # Per example 2, we need to return the length of last WORD -> therefore, any trailing spaces are not considered.

        # First, remove trailing " " chars from the end of the word.

        right = len(s) - 1
        while s[right] == " ":
            right -= 1
        # Right pointer is at final index of final word.

        curLength = 0
        for i in range(right + 1):
            if s[i] == " ":
                curLength = 0
            else:
                curLength += 1
        return curLength

# Time Complexity: O(n) -> Traverse entire nums array 1 time.
# Space Complexity: O(1) -> No additional Storage used.



# 2nd Solution:

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Return the length of the last word.
        #   - First split the string by spaces, then return the length of the final element in the array.

        s = s.strip(" ")
        return len(s.split(" ")[-1])

# Time Complexity: O(n) -> Split the string, then return the length of the final element.
# Space Complexity: O(1) -> No additional storage used.