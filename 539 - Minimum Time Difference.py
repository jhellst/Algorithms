# Given a list of 24-hour clock time points in "HH:MM" format, return the minimum minutes difference between any two time-points in the list.

# Example 1:
# Input: timePoints = ["23:59", "00:00"]
# Output: 1

# Example 2:
# Input: timePoints = ["00:00", "23:59", "00:00"]
# Output: 0

# Constraints:
#     2 <= timePoints.length <= 2 * 104
#     timePoints[i] is in the format "HH:MM".


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # Process each time to minutes only. Then, sort (or use heap) and traverse the array, calculating the time difference between the two.
        #   - "23:59" -> 23 * 60 + 59

        min_difference = 24 * 60

        time_point_values = []
        for time in timePoints:
            hours, minutes = time.split(":")
            time_point_values.append(int(hours) * 60 + int(minutes))

        time_point_values.sort()

        prev_time_minutes = time_point_values[0]
        for minutes in time_point_values[1:]:
            diff = abs(minutes - prev_time_minutes)
            min_difference = min(min_difference, diff)

            prev_time_minutes = minutes

        # As a final step, compare the "wrap around" case -> check first vs. last element.
        min_difference = min(min_difference, 24 * 60 -
                             time_point_values[-1] + time_point_values[0])

        return min_difference

# Time Complexity: O(n * log(n)) -> Visit each value in array, then sort array of length n.
# Space Complexity: O(n) -> Store n values in time_point_values array.
