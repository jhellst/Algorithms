# Given an integer n, return all the numbers in the range[1, n] sorted in lexicographical order.
# You must write an algorithm that runs in O(n) time and uses O(1) extra space.

# Example 1:
# Input: n = 13
# Output: [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]

# Example 2:
# Input: n = 2
# Output: [1, 2]

# Constraints:
#     1 <= n <= 5 * 104


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        # Process each digit of n separately.
        #   - So, for 13 -> do first digit (0, 1) AND do second digit (0, 1, 2, 3)
        #   - For each digit, it can be zero. This might lead to the leading number being different.

        # DFS-style solution. We need to "traverse" in-order, in terms of starting at the lowest and ending at the highest.

        res = [str(val) for val in range(1, n + 1)]
        res.sort()
        return [int(val) for val in res]

# Time Complexity: O(n * log(n)) -> Traverse range of 1 to n, then sort array of n items.
# Space Complexity: O(1) -> No additional storage space used.
