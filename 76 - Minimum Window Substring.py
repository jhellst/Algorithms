# Given two strings s and t of lengths m and n respectively, return the minimum window substring
# of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".
# The testcases will be generated such that the answer is unique.

# Example 1:

# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

# Example 2:

# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.

# Example 3:

# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.



# Constraints:

#     m == s.length
#     n == t.length
#     1 <= m, n <= 105
#     s and t consist of uppercase and lowercase English letters.


# Follow up: Could you find an algorithm that runs in O(m + n) time?


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Create windows of equal length. Window for t is exactly len(t), window for s is len >= len(t).

        def are_chars_in_window(d, window_dict):
            for key in d.keys():
                if window_dict.get(key, 0) < d[key]:
                    return False
            return True


        t_dict = Counter(t) # Contains count of each character in t.
        s_dict = Counter(s[0:len(t)]) # Contains count of each character in current window.

        left = 0
        right = len(t) - 1
        res = ""
        min_len = float("inf")

        while right < len(s):
            while are_chars_in_window(t_dict, s_dict):
                if min_len >= (right - left + 1):
                    res = s[left:right+1]
                    min_len = right - left

                remove_char = s[left]
                s_dict[remove_char] -= 1
                if s_dict[remove_char] == 0:
                    del s_dict[remove_char]
                left += 1
            else:
                right += 1
                if right <= len(s) - 1:
                    add_char = s[right]
                    s_dict[add_char] = s_dict.get(add_char, 0) + 1

        return res