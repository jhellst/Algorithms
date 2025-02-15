# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

# Example 1:

# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.

# Example 2:

# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.

# Constraints:

#     1 <= nums.length <= 100
#     0 <= nums[i] <= 400



class Solution:
    def rob(self, nums: List[int]) -> int:
        # DP-style solution.
        #   - Simulate the robber's decisions -> traverse the array, selecting the more profitable decision at each house.
        #   -> Option 1: Rob from current house, meaning we can't rob from prev or next house.
        #   -> Option 2: Don't rob from current house, meaning we can rob from prev and/or next house.

        if len(nums) < 2:
            return max(nums)

        amount_taken = [0] * len(nums)
        amount_taken[0] = nums[0]
        amount_taken[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            # Simulate the most profitable action -> either take (cur val + 2 houses ago) OR don't take (max val of 1 and 2 houses ago).
            amount_taken[i] = max(amount_taken[i - 2] + nums[i], amount_taken[i - 1])

        return max(amount_taken[-1], amount_taken[-2])

# Time Complexity: O(n) -> Traverse array of length n.
# Space Complexity: O(n) -> Store max_amount_taken for each house in array of length n.