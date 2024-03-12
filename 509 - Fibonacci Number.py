# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.
# Given n, calculate F(n).


# Example 1:
# Input: n = 2
# Output: 1
# Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

# Example 2:
# Input: n = 3
# Output: 2
# Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

# Example 3:
# Input: n = 4
# Output: 3
# Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.


class Solution:
    def fib(self, n: int) -> int:
        # Dynamic programming solution. Want to reference the previous 2 values from dp dictionary.

        dp = {0: 0, 1: 1}

        for i in range(2, n + 1):
            dp[i] = dp[i - 2] + dp[i - 1]

        return dp[n]

# Time Complexity: O(n) -> Single pass of 2 through n.
# Space Complexity: O(n) -> Each value (0 through n) is stored once in dp.