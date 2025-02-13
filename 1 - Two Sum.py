# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Unsorted array has exactly 1 correct answer.
        # Use a set/hashmap to store values as we traverse nums. Also possible to sort array, IF we use list comprehension to also store indices.

        seen = {} # num:index

        for i, num in enumerate(nums):
            if target - num in seen:
                return [i, seen[target - num]]
            else:
                seen[num] = i

# Time Complexity: O(n) -> Single pass of nums array.
# Space Complexity: O(n) -> Store up to every number in nums in hashmap.




# 2nd Solution:

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Need to find target sum from 2 values in nums array.
        #   - We can use a hashmap (or sort and use 2-pointers).

        # Process:
        #   - Check to see if (target - num) is in the hashmap -> if it is, return the solution.
        #   - Add num to the hashmap with its index as the stored value.
        #   - Continue to process each value in nums.

        hash_map = {} # val:index

        for i, num in enumerate(nums):
            if (target - num) in hash_map:
                return [i, hash_map[target - num]]
            hash_map[num] = i

# Time Complexity: O(n) -> Traverse nums array once (at most).
# Space Complexity: O(n) -> Store every value in nums in hash_map.



# 3rd Solution:

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Find the indices of the 2 values that sum to target. There is exactly 1 answer.
        # Use a hashmap to store value:index. If (target - cur_val) is in the hashmap, we have a match!

        hashmap = {} # val:index
        for i, val in enumerate(nums):
            if (target - val) in hashmap:
                return [i, hashmap[target - val]]
            hashmap[val] = i

# Time Complexity: O(n) -> In worst case, visit every index one time.
# Space Complexity: O(n) -> In worst case, store every val:index pair in a hashmap.