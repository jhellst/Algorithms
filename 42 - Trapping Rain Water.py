# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

# Example 1:

# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

# Example 2:

# Input: height = [4,2,0,3,2,5]
# Output: 9

# Constraints:

# n == height.length
# 1 <= n <= 2 * 104
# 0 <= height[i] <= 105


class Solution:
    def trap(self, height: List[int]) -> int:
        # 2-pointers. Need to narrow the range from the outside moving in. Use a greedy-style algorithm to determine which pointer to move.

        left, right = 0, len(height) - 1
        leftMax, rightMax = height[left], height[right]
        totalVolume = 0

        while left < right:
            if height[left] < height[right]: # Left is shorter, increment left pointer.
                totalVolume += leftMax - height[left]
                left += 1
                leftMax = max(height[left], leftMax)

            else:
                totalVolume += rightMax - height[right]
                right -= 1
                rightMax = max(height[right], rightMax)

        return totalVolume

# Time Complexity: O(n) -> Single pass of array with 2 pointers.
# Space Complexity: O(1) -> No additional storage used.



# 2nd Solution:
class Solution:
    def trap(self, height: List[int]) -> int:
        # Use 2 pointers to "trap" rain water while moving inwards from both sides.
        # Greedily select the lower side to increment inwards first -> this will prevent issues with duplicate counting.

        left, right = 0, len(height) - 1
        leftMax, rightMax = height[left], height[right]
        waterVolume = 0

        while left < right:
            leftH, rightH = height[left], height[right]
            if leftH <= rightH:
                waterVolume += max(0, leftMax - leftH)
                left += 1
                leftMax = max(leftH, leftMax)
            else:
                waterVolume += max(0, rightMax - rightH)
                right -= 1
                rightMax = max(rightH, rightMax)

        return waterVolume

# Time Complexity: O(n) -> Single pass of array with 2 pointers from each end.
# Space Complexity: O(1) -> No additional storage used.



# 3rd Solution:

class Solution:
    def trap(self, height: List[int]) -> int:
        # Greedy solution. Start with 2 pointers and increment inwards from the shorter side.
        #   - Track max_height from each side and calculate volume_added based based on 1 * (max_height - cur_height).

        volume_captured = 0

        left, right = 0, len(height) - 1
        max_left, max_right = height[left], height[right]
        while left < right:
            # Increment from the shorter side, to avoid "missing" any captured volume.
            if height[left] < height[right]:
                volume_captured += (max_left - height[left])
                left += 1
                max_left = max(max_left, height[left])
            else:
                volume_captured += (max_right - height[right])
                right -= 1
                max_right = max(max_right, height[right])

        return volume_captured

# Time Complexity: O(n) -> Traverse each item in height array one time.
# Space Complexity: O(1) -> No additional storage used.