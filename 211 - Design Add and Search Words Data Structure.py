# Design a data structure that supports adding new words and finding if a string matches any previously added string.

# Implement the WordDictionary class:

# WordDictionary() Initializes the object.
# void addWord(word) Adds word to the data structure, it can be matched later.
# bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.


# Example:

# Input
# ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
# [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
# Output
# [null,null,null,null,false,true,true,true]

# Explanation
# WordDictionary wordDictionary = new WordDictionary();
# wordDictionary.addWord("bad");
# wordDictionary.addWord("dad");
# wordDictionary.addWord("mad");
# wordDictionary.search("pad"); // return False
# wordDictionary.search("bad"); // return True
# wordDictionary.search(".ad"); // return True
# wordDictionary.search("b.."); // return True


class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        curLevel = self.trie
        for char in word:
            if char in curLevel:
                curLevel = curLevel[char]
            else:
                curLevel[char] = {}
                curLevel = curLevel[char]

        # End of word, add "#" to indicate it's a complete word.
        curLevel["#"] = {}


    def search(self, word: str) -> bool:

        trieLevel = self.trie

        def searchLevel(word, trieLevel):

            if not word:
                if "#" in trieLevel:
                    return True
                else:
                    return False

            curChar = word[0]

            if curChar in trieLevel:
                if searchLevel(word[1:], trieLevel[curChar]):
                    return True

            elif curChar == ".": # Search all possible paths on this level.
                for char in trieLevel:
                    if searchLevel(word[1:], trieLevel[char]):
                        return True
            else:
                return False # Char is not in trie.

        return searchLevel(word, trieLevel)

# Time Complexity:
    # init: O(1)
    # addWord: O(n) -> traverse the string and dict at max 1 time for each char.
    # search: O(n * 26) -> O(n) -> Worst case is that each char is "." -> Need to visit every node in the trie, with a max of 26 chars per level.


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)



# Constraints:

# 1 <= word.length <= 25
# word in addWord consists of lowercase English letters.
# word in search consist of '.' or lowercase English letters.
# There will be at most 2 dots in word for search queries.
# At most 104 calls will be made to addWord and search.




# 2nd solution:

class WordDictionary:
    # Use a Trie data structure. Will construct words in the trie, level-by-level (char-by-char).

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        trieLevel = self.trie

        for char in word:
            if char not in trieLevel:
                trieLevel[char] = {}
            trieLevel = trieLevel[char]
        trieLevel["*"] = {}

    def search(self, word: str) -> bool:
        # Searches the trie for a word. Word can contain "." chars which are wildcards.
        # Recursive definition is simple to implement here.

        def dfs(word, index, trieLevel):
            if index == len(word):
                if "*" in trieLevel:
                    return True
                else:
                    return False

            if word[index] == ".":
                for char in trieLevel:
                    if dfs(word, index + 1, trieLevel[char]):
                        return True
                return False
            elif word[index] not in trieLevel:
                return False
            else:
                return dfs(word, index + 1, trieLevel[word[index]])

        return dfs(word, 0, self.trie)

# Time Complexity:
#   - Init: O(1)
#   - addWord: O(n) -> In every case, traverse through every char of the word and advance in trie / add to trie.
#   - search: O(n * 26) -> O(n) -> In worst case, (all chars are "."), we need to check every item in every level. Every level contains, at most, 26 characters to check.

# Space Complexity:
#   - addWord: O(n) -> Store each character in trie, on a different level.
#   - search: O(m) -> where m is the length of the longest word -> Worst case involves searching for the longest word. Call stack can contain 1 function call for each level of the trie.
#       - O(1) for any search that doesn't include any "." characters.