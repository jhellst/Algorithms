# Given a string s which consists of lowercase or uppercase letters, return the length of the longest
# palindrome
#  that can be built with those letters.

# Letters are case sensitive, for example, "Aa" is not considered a palindrome.



# Example 1:

# Input: s = "abccccdd"
# Output: 7
# Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
# Example 2:

# Input: s = "a"
# Output: 1
# Explanation: The longest palindrome that can be built is "a", whose length is 1.


# Constraints:

# 1 <= s.length <= 2000
# s consists of lowercase and/or uppercase English letters only.



class Solution:
    def longestPalindrome(self, s: str) -> int:
        # Calculate the max length of a palindrome that we can create with these letters.
        # We can take even count of every character. We can also take 1 odd count of letters (1, 3, 5, etc.)

        c = collections.Counter(s)
        res = 0
        max_odd_count = 0

        for key in c:
            if c[key] % 2 == 0:
                res += c[key]
            else: # Even count.
                if max_odd_count:
                    if max_odd_count < c[key]:
                        res += max_odd_count - 1
                        max_odd_count = c[key]
                    else:
                        res += c[key] - 1
                else:
                    max_odd_count = c[key]

        return res + max_odd_count

# Time Complexity: O(n) -> Create a counter from s and visit each key once.
# Space Complexity: O(n) -> Create a counter that contains up to s # of items. Worst case is where s == n.