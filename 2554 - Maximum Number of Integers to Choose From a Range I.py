# You are given an integer array banned and two integers n and maxSum. You are choosing some number of integers following the below rules:
#     The chosen integers have to be in the range [1, n].
#     Each integer can be chosen at most once.
#     The chosen integers should not be in the array banned.
#     The sum of the chosen integers should not exceed maxSum.

# Return the maximum number of integers you can choose following the mentioned rules.


# Example 1:
# Input: banned = [1,6,5], n = 5, maxSum = 6
# Output: 2
# Explanation: You can choose the integers 2 and 4.
# 2 and 4 are from the range [1, 5], both did not appear in banned, and their sum is 6, which did not exceed maxSum.

# Example 2:
# Input: banned = [1,2,3,4,5,6,7], n = 8, maxSum = 1
# Output: 0
# Explanation: You cannot choose any integer while following the mentioned conditions.

# Example 3:
# Input: banned = [11], n = 7, maxSum = 50
# Output: 7
# Explanation: You can choose the integers 1, 2, 3, 4, 5, 6, and 7.
# They are from the range [1, 7], all did not appear in banned, and their sum is 28, which did not exceed maxSum.

# Constraints:
#     1 <= banned.length <= 104
#     1 <= banned[i], n <= 104
#     1 <= maxSum <= 109



class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        # Return the max # of integers you're able to "choose".
        #   - We want to maximize the count of integers, while still being <= maxSum.
        # Greedy solution. We can loop in range(1, n + 1) and add any number not in banned. Track count.
        #   - If cur_sum <= maxSum, this combo of numbers is valid.

        banned_nums = set(banned)
        cur_sum = 0
        count = 0

        for num in range(1, n + 1):
            if (num + cur_sum > maxSum): # We can't add this number. Return count.
                return count
            if num not in banned_nums:
                count += 1
                cur_sum += num

        return count

# Time Complexity: O(m + n) -> Traverse range of length n, and create a set of size m.
# Space Complexity: O(m) -> Use a set to store up to m banned numbers.