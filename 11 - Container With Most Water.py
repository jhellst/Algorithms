# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.

# Example 1:

# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

# Example 2:

# Input: height = [1,1]
# Output: 1


# Constraints:

# n == height.length
# 2 <= n <= 105
# 0 <= height[i] <= 104


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Need to find the max amount of water held in the container.
        # Start with 2 pointers spanning the entire array. Work inwards, calculating the amount of water at each increment.
        # Increment inwards from the lower-height point. End this once left == right.

        maxWaterHeld = 0
        left, right = 0, len(height) - 1

        while left < right:
            leftHeight, rightHeight = height[left], height[right]
            waterHeld = min(leftHeight, rightHeight) * (right - left)
            maxWaterHeld = max(waterHeld, maxWaterHeld)

            if height[left] > height[right]:
                right -= 1
            else:
                left += 1

        return maxWaterHeld

# Time Complexity: O(n) -> Two pointers, single pass of each item in array.
# Space Complexity: O(1) -> No additional storage needed.