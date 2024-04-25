# The Tribonacci sequence Tn is defined as follows:
# T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
# Given n, return the value of Tn.

# Example 1:

# Input: n = 4
# Output: 4
# Explanation:
# T_3 = 0 + 1 + 1 = 2
# T_4 = 1 + 1 + 2 = 4

# Example 2:

# Input: n = 25
# Output: 1389537

# Constraints:

# 0 <= n <= 37
# The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1.


class Solution:
    def tribonacci(self, n: int) -> int:
        # Dynamic Programming solution.

        dp = {0: 0, 1: 1, 2: 1}

        for i in range(3, n + 1):
            print(i, dp)

            if i not in dp:
                dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1]

        return dp[n]

# Time Complexity: O(n) -> Pass every number from 3 to n.
# Space Complexity: O(n) -> Store every number in range n in a hashmap for DP.