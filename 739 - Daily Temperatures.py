# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

# Example 1:

# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]

# Example 2:

# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]

# Example 3:

# Input: temperatures = [30,60,90]
# Output: [1,1,0]

# Constraints:

# 1 <= temperatures.length <= 105
# 30 <= temperatures[i] <= 100


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Traverse temperatures array and find out how many days it takes to find a warmer temperature at each point.
        # Key Takeaway: At each point, there may be multiple previous temp/index combos that are "looking" for a higher temp.
        #   - Use a stack to store temperatures that are still searching for a warmer temp.
        #   - If the temp DROPS, then we add the new temp to the stack. When a new temp is seen, if it is warmer than the first temp -> it will 100% be warmer than the second temp too.

        res = [0] * len(temperatures)
        stack = [] # [index, temp]

        for i, temp in enumerate(temperatures):
            if stack:
                while stack and stack[-1][1] < temp: # While stack temp is lower than cur temp, pop from stack and record answer in res.
                    prevIndex, prevTemp = stack.pop()
                    res[prevIndex] = i - prevIndex

            stack.append([i, temp]) # Append current index, temp to stack.

        return res

# Time Complexity: O(n) -> Traverse the array once and pop from stack up to 1 time.
# Space Complexity: O(n) -> Using a stack as additional storage, can store each item in array up to 1 time.