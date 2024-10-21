# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
# Return true if you can reach the last index, or false otherwise.

# Example 1:

# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

# Example 2:

# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

# Constraints:

#     1 <= nums.length <= 104
#     0 <= nums[i] <= 105



class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Greedy solution (or DP). We don't need the optimal path -> we just need to see if it is possible.
        #   - Start from final index and see if we can reduce index to 0. Return True if this is possible.

    # Greedy Solution:
    #   - We know that index 0 is the starting position and we need to arrive at index == len(nums) - 1.

        goal = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            max_jump = nums[i]
            if i + max_jump >= goal: # If current jump can reach goal, then we can reach goal from current index. Reset goal == i.
                goal = i

        return goal == 0

# Time Complexity: O(n) -> Traverse every element in the array up to 1 time.
# Space Complexity: O(1) -> No additional storage space used.