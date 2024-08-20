# Given an integer array nums of unique elements, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.

# Example 1:

# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

# Example 2:

# Input: nums = [0]
# Output: [[],[0]]

# Constraints:

# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# All the numbers of nums are unique.


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Backtracking.
        # Note: Elements are unique, so no need to prevent duplication.

        res = []

        def backtrack(i, subset):

            if i >= len(nums):
                res.append(subset[::]) # Only append here -> every combo will terminate here.
                return

            # Backtracking step:

            # Add current num and continue.
            subset.append(nums[i])
            backtrack(i + 1, subset)

            subset.pop()
            backtrack(i + 1, subset)
            return


        backtrack(0, [])
        return res

# Time Complexity: O(n * 2^n)
# Space Complexity: O(n) -> Recursive calls equal to n.