# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

# Example 1:
# Input: nums = [1,2,3,1], k = 3
# Output: true

# Example 2:
# Input: nums = [1,0,1,1], k = 1
# Output: true

# Example 3:
# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false

# Constraints:
#     1 <= nums.length <= 105
#     -109 <= nums[i] <= 109
#     0 <= k <= 105



class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Use a hash_map -> Store each value as we see it, along with its index.
        #   - If we see that value again, check for 2nd condition -> abs(i - j) <= k:

        hash_map = {} # num:set(idx1, idx2, ...)

        for i, num in enumerate(nums):

            if num in hash_map: # We have a duplicate value. We want to check validity of every index in hash_map[num].
                for idx2 in hash_map[num]:
                    if (abs(i - idx2) <= k):
                        return True
            else:
                hash_map[num] = set()
            hash_map[num].add(i)

        return False

# Time Complexity: O(n) -> Traverse each num in nums in worst case.
# Space Complexity: O(n) -> In worst case, store every value in hash_map data structure.