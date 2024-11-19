# You are given a positive integer days representing the total number of days an employee is available for work (starting from day 1). You are also given a 2D array meetings of size n where, meetings[i] = [start_i, end_i] represents the starting and ending days of meeting i (inclusive).
# Return the count of days when the employee is available for work but no meetings are scheduled.
# Note: The meetings may overlap.

# Example 1:
# Input: days = 10, meetings = [[5,7],[1,3],[9,10]]
# Output: 2
# Explanation:
# There is no meeting scheduled on the 4th and 8th days.

# Example 2:
# Input: days = 5, meetings = [[2,4],[1,3]]
# Output: 1
# Explanation:
# There is no meeting scheduled on the 5th day.

# Example 3:
# Input: days = 6, meetings = [[1,6]]
# Output: 0
# Explanation:
# Meetings are scheduled for all working days.

# Constraints:
#     1 <= days <= 109
#     1 <= meetings.length <= 105
#     meetings[i].length == 2
#     1 <= meetings[i][0] <= meetings[i][1] <= days



class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        # We want to find the number of days that a meeting occurs on -> merge intervals to find the total range.
        #   - Then, return -> available_days - meeting_days

        meeting_days = 0
        meetings.sort()
        cur_interval = meetings[0]

        for start, end in meetings[1:]:
            if cur_interval[1] < start: # No overlap, and cur_interval can be appended.
                meeting_days += (cur_interval[1] - cur_interval[0] + 1)
                cur_interval = [start, end]
            else: # Some overlap.
                cur_interval = [min(start, cur_interval[0]), max(end, cur_interval[1])]

        if cur_interval:
            meeting_days += (cur_interval[1] - cur_interval[0] + 1)

        return days - meeting_days

# Time Complexity: O(n + n*log(n)) -> O(n*log(n)) -> Sort meetings array, then visit each element once.
# Space Complexity: O(1) -> No additional storage used.