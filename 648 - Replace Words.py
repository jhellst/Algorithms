# In English, we have a concept called root, which can be followed by some other word to form another longer word - let's call this word derivative. For example, when the root "help" is followed by the word "ful", we can form a derivative "helpful".
# Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces, replace all the derivatives in the sentence with the root forming it. If a derivative can be replaced by more than one root, replace it with the root that has the shortest length.
# Return the sentence after the replacement.


# Example 1:

# Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
# Output: "the cat was rat by the bat"

# Example 2:

# Input: dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
# Output: "a a b c"

# Constraints:

# 1 <= dictionary.length <= 1000
# 1 <= dictionary[i].length <= 100
# dictionary[i] consists of only lower-case letters.
# 1 <= sentence.length <= 106
# sentence consists of only lower-case letters and spaces.
# The number of words in sentence is in the range [1, 1000]
# The length of each word in sentence is in the range [1, 1000]
# Every two consecutive words in sentence will be separated by exactly one space.
# sentence does not have leading or trailing spaces.


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        # Split the string into a list, then use an algorithm to "replace" each split elem with the shortest corresponding one.
        # Use a set to store the roots and access them.

        self.words = set(dictionary)
        self.min_length, self.max_length = inf, -inf

        res = []
        for word in sentence.split(" "):
            res.append(self.find_root(word))

        return " ".join(res)


    # Helper function to return the root (or the original).
    def find_root(self, word):
        """Given a word, returns the shortest valid matching root from the dictionary."""

        cur_root = ""

        for i in range(len(word)): # Add the minimum # of characters to find a match.
            cur_root += word[i]

        # Now, continue to look for a match. Every time you can't find a match, add the next character to cur_root.
        # Note: If we pass up the max_length, then we can return the original word.

            if cur_root in self.words:
                return cur_root

        return word

# Time Complexity: O(n * m) -> Create a set of length n, and in worst case each word will be the same length m.
# Space Complexity: O(n) -> Create a set of size n, create res array of size n.