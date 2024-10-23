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


# 2nd Solution:

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Want to find the minimum cost required to reach the last index.
        # DP-style solution. At each space, we'll store the minimum cost to reach that space.
        #   - To simulate a "step", we are able to go 1 OR 2 steps ahead.

        min_cost = [0] * len(cost)
        min_cost[0], min_cost[1] = cost[0], cost[1]

        for i in range(2, len(min_cost)): # For each step, store the minumum cost to get there -> need to look back 1 and 2 spaces.
            min_cost[i] = cost[i] + min(min_cost[i - 1], min_cost[i - 2])

        return min(min_cost[-1], min_cost[-2])

# Time Complexity: O(n) -> Traverse cost array once.
# Space Complexity: O(n) -> Store dp in array of length n.


# 2nd Solution:

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Dynamic programming. We want to traverse the staircase while simulating the min_steps it takes to reach each space (as we reach it).
        #   - We can take either 1 or 2 steps.
        #   - We can start at index 0 or 1.

        total_cost = [inf] * len(cost)
        total_cost[0], total_cost[1] = cost[0], cost[1]

        for i in range(2, len(cost)): # Loop through every index after 0 and 1, storing min_steps.
            total_cost[i] = min(total_cost[i - 1], total_cost[i - 2]) + cost[i]

        return min(total_cost[-1], total_cost[-2])

# Time Complexity: O(n) -> Traverse array once.
# Space Complexity: O(n) -> Store values in array of len(n).