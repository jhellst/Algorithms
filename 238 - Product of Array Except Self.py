# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

# Constraints:

# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Must run in O(n) time, so looking for a single-pass solution.
        # Intuition is to use a prefix-product and postfix-product, and recalculate these as we traverse the array.

        res = [1] * len(nums)
        prefixes = [1] * len(nums)
        postfixes = [1] * len(nums)

        # First populate prefix products while traversing nums.
        prefix = 1
        for i, num in enumerate(nums):
            prefixes[i] = prefix
            prefix *= num

        postfix = 1
        # Then, populate postfix products while traversing nums backwards.
        for i in range(len(nums) - 1, -1, -1):
            postfixes[i] = postfix
            postfix *= nums[i]

        # Final Step: Traverse the array and calculate from product of prefix and postfix at that index.
        for i in range(0, len(nums)):
            res[i] = prefixes[i] * postfixes[i]

        return res


# Time Complexity: O(3n) -> O(n) -> Traverse nums array 3 times.
# Space Complexity: O(2n) -> O(n) -> Store n values in 2 separate arrays (prefixes and postfixes).




# 2nd Solution - Optimal Solution with O(1) Space:

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Important Takeaway: The occurence of zeroes in the array makes things much more complicated for a single-pass.
        #   - To simplify, we can first check for the count of zeroes in the array.

        # A few different main cases:
        #   1) No zeroes in array -> All products can be calculated in one-pass.
        #   2) 1 zero in array -> All products are 0, except for the index where 0 was initially (product of all other nums).
        #   3) Multiple zeroes in array -> Every product in the array is 0.

        num_zeroes = nums.count(0)

        if num_zeroes >= 2: # Answer will be all zeroes.
            return [0] * len(nums)

        if num_zeroes == 0: # We can process the array's product while traversing once.
            res = []

            cur_product = 1
            for num in nums:
                cur_product *= num
            # Now cur_product is the product of all numbers -> value at index 0.

            prev = None
            for num in nums:
                if prev:
                    cur_product *= prev
                cur_product = cur_product // num
                res.append(cur_product)

                prev = num

            return res

        if num_zeroes == 1: # The 0 will be replaced with the final product and every other number will be 0.

            cur_product = 1
            zero_index = None
            for i, num in enumerate(nums):
                if num == 0:
                    zero_index = i
                else:
                    cur_product *= num

            res = [0] * len(nums)
            res[zero_index] = cur_product
            return res

# Time Complexity: O(n) -> Multiple passes of array of length n.
# Space Complexity: O(1) -> No additional storage space used.



# 3rd Solution:

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # We can use a prefix_product as we traverse the array.
        # Important restriction: If there are zeroes, we need more logic to prevent dividing by zero.
        #   - We can use zero_count to inform how we'll interact with this array.

        res = [0] * len(nums)
        zero_count = nums.count(0)

        if zero_count == 0: # Normal processing with cur_product tracked.

            cur_product = 1
            for num in nums:
                cur_product *= num
            # Now we have cur_product for every num in nums. Start back at first num, processing the cur_product with multiplication/division.

            for i, num in enumerate(nums):
                cur_product = cur_product // num
                res[i] = cur_product
                cur_product *= num

            return res

        elif zero_count == 1:
            # Every space will be zero, and the index with 0 initially will be the product of every other number in the array.
            cur_product = 1
            for num in nums:
                if num != 0:
                    cur_product *= num

            for i, num in enumerate(nums):
                if num == 0:
                    nums[i] = cur_product
                else:
                    nums[i] = 0

            return nums

        else: # Multiple zeroes in array, all elements will be zero.
            return [0] * len(nums)


# Time Complexity: O(n) -> Traverse nums array multiple times.
# Space Complexity: O(1) -> No additional storage used.