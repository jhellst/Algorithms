# A critical point in a linked list is defined as either a local maxima or a local minima.
# A node is a local maxima if the current node has a value strictly greater than the previous node and the next node.
# A node is a local minima if the current node has a value strictly smaller than the previous node and the next node.
# Note that a node can only be a local maxima/minima if there exists both a previous node and a next node.
# Given a linked list head, return an array of length 2 containing [minDistance, maxDistance] where minDistance is the minimum distance between any two distinct critical points and maxDistance is the maximum distance between any two distinct critical points. If there are fewer than two critical points, return [-1, -1].

# Example 1:

# Input: head = [3,1]
# Output: [-1,-1]
# Explanation: There are no critical points in [3,1].

# Example 2:

# Input: head = [5,3,1,2,5,1,2]
# Output: [1,3]
# Explanation: There are three critical points:
# - [5,3,1,2,5,1,2]: The third node is a local minima because 1 is less than 3 and 2.
# - [5,3,1,2,5,1,2]: The fifth node is a local maxima because 5 is greater than 2 and 1.
# - [5,3,1,2,5,1,2]: The sixth node is a local minima because 1 is less than 5 and 2.
# The minimum distance is between the fifth and the sixth node. minDistance = 6 - 5 = 1.
# The maximum distance is between the third and the sixth node. maxDistance = 6 - 3 = 3.

# Example 3:

# Input: head = [1,3,2,2,3,2,2,2,7]
# Output: [3,3]
# Explanation: There are two critical points:
# - [1,3,2,2,3,2,2,2,7]: The second node is a local maxima because 3 is greater than 1 and 2.
# - [1,3,2,2,3,2,2,2,7]: The fifth node is a local maxima because 3 is greater than 2 and 2.
# Both the minimum and maximum distances are between the second and the fifth node.
# Thus, minDistance and maxDistance is 5 - 2 = 3.
# Note that the last node is not considered a local maxima because it does not have a next node.

# Constraints:

# The number of nodes in the list is in the range [2, 105].
# 1 <= Node.val <= 105


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        # Find "critical points" (local min and max). Criteria -> if node is smaller/larger than both prev and next nodes.
        #   - Mark the indices/counts of critical points, and recalculate the min/max as you observe each additional critical point.

        res = [None, None]
        critical_points = []

        cur_index = 0
        prev_val = None

        while head:

            if prev_val and head.next and head.next != None and ((head.val > prev_val and head.val > head.next.val) or (head.val < prev_val and head.val < head.next.val)):
                print("!", head.val)

                critical_points.append(cur_index)

            cur_index += 1
            prev_val = head.val
            head = head.next

        print(critical_points)

        if len(critical_points) < 2:
            return [-1, -1]

        prev_index = None
        for index in critical_points:

            if prev_index:
                if res[0]:
                    res[0] = min(res[0], index - prev_index)
                else:
                    res[0] = index - prev_index

            if res[1]:
                res[1] = max(res[1], index - critical_points[0])
            else:
                res[1] = index - critical_points[0]

            prev_index = index

        return res

# Time Complexity: O(2 * n) -> O(n) -> Traverse every node in the linked list once, then traverse the critical_points array once.
# Space Complexity: O(n) -> Store points in critical_points array. -> Could be optimized to use no additional storage space.