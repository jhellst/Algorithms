# You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].
# Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:
#     0 <= j <= nums[i] and
#     i + j < n

# Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

# Example 1:

# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

# Example 2:

# Input: nums = [2,3,0,1,4]
# Output: 2


class Solution:
    def jump(self, nums: List[int]) -> int:
        # DP-style solution.
        # For each step, simulate all possible "steps".
        #   - Replace/keep the min count only.

        steps = [inf] * len(nums) # Holds step counts for each (starting at inf, so that every calculated count is lower than initial value).
        steps[0] = 0

        # Bad explanation in problem, but assumption is that "j" is the value at nums[i]
        for cur_index, j in enumerate(nums):
            steps_at_start = steps[cur_index]

            # Loop through range from cur_index.
            for i in range(cur_index, min(cur_index + j + 1, len(nums))):
                steps[i] = min(steps_at_start + 1, steps[i])

        return steps[-1]

# Time Complexity: O(n^2) -> Double-nested loop within nums/steps array.
# Space Complexity: O(n) -> Store values in array of len(nums).