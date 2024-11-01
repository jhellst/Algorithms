# Given a string s, return the number of palindromic substrings in it.
# A string is a palindrome when it reads the same backward as forward.
# A substring is a contiguous sequence of characters within the string.

# Example 1:

# Input: s = "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".

# Example 2:

# Input: s = "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

# Constraints:

#     1 <= s.length <= 1000
#     s consists of lowercase English letters.


class Solution:
    def countSubstrings(self, s: str) -> int:
        # Count every palindromic substring contained within the string.
        # Need to check for palindromes of 1) odd-length and 2) even-length

        count = 0

        # Odd-length.
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1

        # Even-length.
        for i in range(len(s) - 1):
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1

        return count

# Time Complexity: O(n^2) -> Double-nested loop through each index of s.
# Space Complexity: O(1) -> No additional storage used.



# 2nd Solution:

class Solution:
    def countSubstrings(self, s: str) -> int:
        # We want to count the number of palindromic substrings in a string.
        #   - From each index, we want to count the # of substrings expanding (from that center index) that are palindromes.

        res = 0

        # First, check palindromes of odd length at each index.
        for i in range(len(s)):
            count = 0
            first, second = i, i
            while (first - count) >= 0 and (second + count) < len(s) and s[first - count] == s[second + count]:
                count += 1
            # Now, record the number of palindromes.
            res += count

        # Then, check palindromes of odd even at each valid index.
        for i in range(len(s) - 1):
            count = 0
            first, second = i, i + 1
            while (first - count) >= 0 and (second + count) < len(s) and s[first - count] == s[second + count]:
                count += 1
            # Now, record the number of palindromes.
            res += count

        return res

# Time Complexity: O(n^2) -> Loop through every index and potentially check every valid index expanding from that index.
# Space Complexity: O(1) -> No additional storage used.