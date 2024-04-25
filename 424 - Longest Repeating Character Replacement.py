# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.
# Return the length of the longest substring containing the same letter you can get after performing the above operations.

# Example 1:

# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.

# Example 2:

# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# There may exists other ways to achieve this answer too.

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # 2-pointers style solution.
        # As we increase the substring by incrementing right pointer, we evaluate the new character to see if the substring is still valid.
        # If valid, continue incrementing. Use a maxHeap to store the most common character in the substring.

        count = {}
        res = 0
        left = 0

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            if (right - left + 1) - max(count.values()) <= k:
                res = max(res, right - left + 1)
            else:
                count[s[left]] -= 1
                left += 1

        return res

# Time Complexity: O(n) -> Traverse each cell once.
# Space Complexity: O(n) -> Store up to each character once, assuming all characters in string are unqiue.


# Optimal Solution.
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Sliding window. Use a hashmap to store the character counts. Expand to right, and decrement from left whenever the substring isn't valid.

        hashmap = {} # Used to store character counts of current window/substring.
        res = 0
        maxCount = 0

        left = 0
        for right in range(len(s)):
            hashmap[s[right]] = hashmap.get(s[right], 0) + 1
            maxCount = max(maxCount, hashmap[s[right]]) # Recalculate maxCount.

            # Check for validity.
            while right - left + 1 - maxCount > k:
                hashmap[s[left]] -= 1
                left += 1

            # Now, substring is valid and can be compared against res.
            res = max(res, right - left + 1)

        return res

# Time Complexity: O(n) -> Pass over array once with sliding window.
# Space Complexity: O(n) -> Store each char in hashmap, which is n in worst case.