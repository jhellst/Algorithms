# Given an integer array nums, find the subarray with the largest sum, and return its sum.

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.

# Example 2:

# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.
# Example 3:

# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104

# Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadane's Theorem. If we reach a negative TOTAL sum, we can reset the sum and continue.

        res = nums[0]
        curSum = 0

        for num in nums:
            curSum += num
            res = max(res, curSum)
            if curSum <= 0:
                curSum = 0

        return res

# Time Complexity: O(n) -> Single pass of array
# Space Complexity: O(1) -> No additional storage


# 2nd Solution:

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadane's theorem. Whenever the sub_array's sum is < 0, we can reset it greedily.

        cur_sum = nums[0]
        res = cur_sum

        for num in nums[1:]:
            if cur_sum < 0:
                cur_sum = 0

            cur_sum += num
            res = max(res, cur_sum)

        return res

# Time Complexity: O(n) -> Traverse nums array once.
# Space Complexity: O(1) -> No additional storage used.