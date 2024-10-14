# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Example 1:

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

# Example 2:

# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

# Constraints:
#     1 <= n <= 45



class Solution:
    def climbStairs(self, n: int) -> int:
        # DP-style solution. For each "space", we'll have one_prev and two_prev -> these contain the number of ways you can arrive to that space.
        one_prev = 1
        two_prev = 1

        # You can "arrive" at each space from one_prev AND two_prev. Therefore, add one_prev + two_prev.

        for i in range(2, n + 1): # Loop through the range, starting at 2.
            cur_val = one_prev + two_prev
            one_prev = two_prev
            two_prev = cur_val

        return max(one_prev, two_prev)

# Time Complexity: O(n) -> Loop through the range of (2, n).
# Space Complexity: O(1) -> No additional storage used.