# Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

# Example 1:

# Input: nums = [1,5,11,5]
# Output: true
# Explanation: The array can be partitioned as [1, 5, 5] and [11].

# Example 2:

# Input: nums = [1,2,3,5]
# Output: false
# Explanation: The array cannot be partitioned into equal sum subsets.

# Constraints:

#     1 <= nums.length <= 200
#     1 <= nums[i] <= 100


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Return True if you can divide nums into 2 subsets with equal sum.
        #   - Values can be in any order.

        # Important Takeaway: We can always return true if we have a sum that equals total_sum / 2.

        if sum(nums) % 2 != 0: # If odd, we can't find the split using only integers.
            return False
        target = sum(nums) // 2 # This is the number we're trying to add up to.

        dp = set()
        dp.add(0)

        for num in nums:
            next_dp = set() # To replace dp after adding new values.
            for t in dp:
                if (t + num) == target:
                    return True
                next_dp.add(t + num)
                next_dp.add(t)
            dp = next_dp

        return False