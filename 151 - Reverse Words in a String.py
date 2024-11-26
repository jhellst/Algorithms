# Given an input string s, reverse the order of the words.
# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
# Return a string of the words in reverse order concatenated by a single space.
# Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

# Example 1:
# Input: s = "the sky is blue"
# Output: "blue is sky the"

# Example 2:
# Input: s = "  hello world  "
# Output: "world hello"
# Explanation: Your reversed string should not contain leading or trailing spaces.

# Example 3:
# Input: s = "a good   example"
# Output: "example good a"
# Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.

# Constraints:
#     1 <= s.length <= 104
#     s contains English letters (upper-case and lower-case), digits, and spaces ' '.
#     There is at least one word in s.

# Follow-up: If the string data type is mutable in your language, can you solve it in-place with O(1) extra space?



class Solution:
    def reverseWords(self, s: str) -> str:
        # Reverse each word in the string. Words are separated by at least one space.
        # Note: Need to reduce all spaces into a single space.

        # First, traverse string and remove any repeated spaces.
        prev = None
        s = s.strip()
        new_string = ""
        for char in s:
            if not (char == " " and prev == " "):
                new_string += char
            prev = char

        # Now, split each word by " " -> then, add each word to a new string in reverse order.
        string_to_array = new_string.split(" ")
        res = ""
        for i in range(len(string_to_array) - 1, -1, -1):
            res += string_to_array[i] + " "
        return res[:-1]

# Time Complexity: O(n) -> Visit every char in the string.
# Space Complexity: O(n) -> Store every char in array.