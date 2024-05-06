# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation:
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.

# Example 2:

# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.

# Example 3:

# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.

# Constraints:

# 3 <= nums.length <= 3000
# -105 <= nums[i] <= 105



class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort nums array and process with 3 pointers.
        # Need to prevent duplicate values.

        res = []
        nums.sort()

        for i, num in enumerate(nums):
            if num > 0:
                break
            elif i > 0 and nums[i - 1] == num: # Prevent using same value as previous loop.
                continue

            l, r = i + 1, len(nums) - 1 # 2 pointers at either end of the remaining range.

            while l < r:
                threeSum = num + nums[l] + nums[r]
                if threeSum == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l - 1] == nums[l]:
                        l += 1

                elif threeSum > 0: # Sum is too large, decrease from right side.
                    r -= 1
                else:
                    l += 1

        return res

# Time Complexity: O(n*log(n)) + O(n^2) -> O(n^2) -> Sort array of length n AND traverse entire array with 2 pointers for each index we visit.
# Space Complexity: O(1) -> No additional storage used.