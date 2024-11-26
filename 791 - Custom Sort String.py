# You are given two strings order and s. All the characters of order are unique and were sorted in some custom order previously.
# Permute the characters of s so that they match the order that order was sorted. More specifically, if a character x occurs before a character y in order, then x should occur before y in the permuted string.
# Return any permutation of s that satisfies this property.

# Example 1:
# Input: order = "cba", s = "abcd"
# Output: "cbad"
# Explanation: "a", "b", "c" appear in order, so the order of "a", "b", "c" should be "c", "b", and "a".
# Since "d" does not appear in order, it can be at any position in the returned string. "dcba", "cdba", "cbda" are also valid outputs.

# Example 2:
# Input: order = "bcafg", s = "abcd"
# Output: "bcad"
# Explanation: The characters "b", "c", and "a" from order dictate the order for the characters in s. The character "d" in s does not appear in order, so its position is flexible.
# Following the order of appearance in order, "b", "c", and "a" from s should be arranged as "b", "c", "a". "d" can be placed at any position since it's not in order. The output "bcad" correctly follows this rule. Other arrangements like "dbca" or "bcda" would also be valid, as long as "b", "c", "a" maintain their order.

# Constraints:
#     1 <= order.length <= 26
#     1 <= s.length <= 200
#     order and s consist of lowercase English letters.
#     All the characters of order are unique.



class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # Use "order" to inform the final arrangement of s.
        # First, create a dict that tracks order_num:char -> we'll use this later to re-order s.
        # Note: If char in s isn't in order, then it can be anywhere in the string -> I'll add them to the end.

        res = ""
        end = ""

        char_order = {}
        for i, char in enumerate(order):
            char_order[i] = char

        c = Counter(s)

        for i in range(0, len(order)):
            if char_order[i] in c: # Char is in order string.
                res += char_order[i] * c[char_order[i]]

        # We also want to add all non-ordered chars to the end of the result.
        for char in s:
            if char not in order:
                end += char

        return res + end

# Time Complexity: O(2n + 2s) -> O(n + s) -> Create counter from s and create dict from order. Then, traverse the dict's keys and the string s once more.
# Space Complexity: O(n + s) -> In worst case, store n keys in order array, and store s chars in dict.