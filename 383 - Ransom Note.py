# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.

# Example 1:

# Input: ransomNote = "a", magazine = "b"
# Output: false

# Example 2:

# Input: ransomNote = "aa", magazine = "ab"
# Output: false

# Example 3:

# Input: ransomNote = "aa", magazine = "aab"
# Output: true

# Constraints:

#     1 <= ransomNote.length, magazine.length <= 105
#     ransomNote and magazine consist of lowercase English letters.



class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Can we construct ransomNote with letters in magazine (count-dependent)?
        #   - Use a hashmap/counter to compare.

        c = Counter(magazine)

        for char in ransomNote:
            if char not in c:
                return False
            c[char] -= 1
            if c[char] == 0:
                del c[char]
        return True

# Time Complexity: O(n + m) -> Create counter from magazine, and in worst case traverse the entire ransomNote string.
# Space Complexity: O(m) -> Create counter with chars from magazine.