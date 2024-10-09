# You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.
# You can either start from the step with index 0, or the step with index 1.
# Return the minimum cost to reach the top of the floor.

# Example 1:

# Input: cost = [10,15,20]
# Output: 15
# Explanation: You will start at index 1.
# - Pay 15 and climb two steps to reach the top.
# The total cost is 15.

# Example 2:

# Input: cost = [1,100,1,1,1,100,1,1,100,1]
# Output: 6
# Explanation: You will start at index 0.
# - Pay 1 and climb two steps to reach index 2.
# - Pay 1 and climb two steps to reach index 4.
# - Pay 1 and climb two steps to reach index 6.
# - Pay 1 and climb one step to reach index 7.
# - Pay 1 and climb two steps to reach index 9.
# - Pay 1 and climb one step to reach the top.
# The total cost is 6.

# Constraints:

#     2 <= cost.length <= 1000
#     0 <= cost[i] <= 999


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # DP-style solution. Can start at 0 or 1.
        # You can step 1 or 2 spaces -> take the minimum cost of the step to every space.

        min_costs = [0] * len(cost)
        min_costs[0] = cost[0]
        min_costs[1] = cost[1]

        for i in range(2, len(cost)):
            cur_cost = cost[i] + min(min_costs[i - 1], min_costs[i - 2])
            min_costs[i] = cur_cost

        return min(min_costs[-1], min_costs[-2])

# Time Complexity: O(n) -> Traverse range of (2, n) exactly one time.
# Space Complexity: O(n) -> Store min_costs in array of length n.