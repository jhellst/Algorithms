# Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.

# Example 1:

# Input: intervals = [[0,30],[5,10],[15,20]]
# Output: false

# Example 2:

# Input: intervals = [[7,10],[2,4]]
# Output: true

# Constraints:
#     0 <= intervals.length <= 104
#     intervals[i].length == 2
#     0 <= starti < endi <= 106



class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # Determine if a person could attend every meeting in intervals.
        #   - Key is to find if there's any overlap in meeting times.

        if not intervals:
            return True

        intervals.sort()
        prev_end = intervals[0][1]

        for start, end in intervals[1:]:
            if prev_end > start:
                return False
            else:
                prev_end = end

        return True

# Time Complexity: O(n * log(n)) -> Sort intervals once, then traverse every item in intervals.
# Space Complexity: O(1) -> No additional storage space used (besides for sorting).