# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
# In other words, return true if one of s1's permutations is the substring of s2.

# Example 1:

# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").

# Example 2:

# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false

# Constraints:

# 1 <= s1.length, s2.length <= 104
# s1 and s2 consist of lowercase English letters.


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # 2-pointers / Sliding-window solution. We want to construct the curDict of chars that are including in the substring. Compare this with s1.

        if len(s1) > len(s2):
            return False
        elif s1 == s2:
            return True

        curDict = {} # Dict to hold
        c = collections.Counter(s1) # Dict to match with for a TRUE response.
        left, right = 0, 0

        for i in range(len(s1)):
            curDict[s2[i]] = curDict.get(s2[i], 0) + 1
            right += 1

        if curDict == c:
            return True

        # Now, traverse the grid with the sliding window at a fixed length.

        while right < len(s2):
            curDict[s2[left]] = curDict.get(s2[left], 0) - 1
            curDict[s2[right]] = curDict.get(s2[right], 0) + 1
            if curDict.get(s2[left], 0) == 0:
                del curDict[s2[left]]
            left += 1
            right += 1
            if curDict == c:
                return True

        return False

# Time Complexity: O(n) -> Single pass of each element in array, exactly 2 times.
# Space Complexity: O(n) -> Store each char in s1 up to once in dict. 2nd dict to also store all chars in s2.



# 2nd Solution: Better space complexity using array for storing letter counts.

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Use a sliding window of length == len(s1), traverse the string and look for permutation matches.
        # - Maintain a size of exactly len(s1).
        # Use a dict or an array of length 26 to store letter_counts as we slide the window.

        if len(s1) > len(s2):
            return False
        elif len(s1) == 1:
            return s1[0] in s2

        letter_count = [0] * 26 # One index for each letter a-z.
        s1_letter_count = [0] * 26 # Represents the letter counts from s1.

        for char in s1:
            cur_letter_index = ord(char) - ord('a')
            s1_letter_count[cur_letter_index] += 1

        left, right = 0, -1

        for char_index in range(len(s1)):
            right += 1
            cur_letter = s2[char_index]
            cur_letter_index = ord(cur_letter) - ord('a')
            letter_count[cur_letter_index] += 1

        if letter_count == s1_letter_count:
            return True

        # Now, we can slide the window, updating letter_count. As we do this, compare with s1_letter_count and return true if that condition is met.
        while right < len(s2) - 1:
            letter_to_remove = s2[left]
            remove_letter_index = ord(letter_to_remove) - ord('a')
            letter_count[remove_letter_index] -= 1
            left += 1

            right += 1
            letter_to_add = s2[right]
            add_letter_index = ord(letter_to_add) - ord('a')
            letter_count[add_letter_index] += 1

            if letter_count == s1_letter_count:
                return True

        if letter_count == s1_letter_count:
            return True

        return False

# Time Complexity: O(n) -> Traverse the array with a sliding window exactly 1 time (visit each character up to 2 times).
# Space Complexity: O(1) -> Constant space, using an array of fixed length == 26.


# 2nd Solution:

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Sliding window of size len(s2).
        #   - Count each time that the char_counts match.
        #   - In theory, we can use an array of length 26 to store counts to improve time complexity.

        if len(s1) > len(s2):
            return False
        elif len(s1) == 1:
            return s1[0] in s2

        s1_char_count = [0] * 26
        s2_char_count = [0] * 26

        left, right = 0, -1

        for i in range(len(s1)):
            right += 1

            s1_char_index = ord(s1[right]) - ord('a')
            s2_char_index = ord(s2[right]) - ord('a')

            s1_char_count[s1_char_index] += 1
            s2_char_count[s2_char_index] += 1


        # Now, each array is populated with the starting count. Continue to "slide" the window and check for equality.

        if s1_char_count == s2_char_count:
            return True

        while right < len(s2) - 1: # Check equality, then remove far left char and add new right char.

            if s1_char_count == s2_char_count:
                return True

            # Remove far left char.
            left_char = s2[left]
            left_char_index = ord(left_char) - ord('a')
            s2_char_count[left_char_index] -= 1
            left += 1

            right += 1
            right_char = s2[right]
            right_char_index = ord(right_char) - ord('a')
            s2_char_count[right_char_index] += 1

            if s1_char_count == s2_char_count:
                return True


        if s1_char_count == s2_char_count:
            return True
        else:
            return False

# Time Complexity: O(n) -> Traverse s2 exactly one time.
# Space Complexity: O(1) -> Store counts in 2 arrays of length 26 -> constant time.