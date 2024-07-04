# You are given the head of a linked list, which contains a series of integers separated by 0's. The beginning and end of the linked list will have Node.val == 0.
# For every two consecutive 0's, merge all the nodes lying in between them into a single node whose value is the sum of all the merged nodes. The modified list should not contain any 0's.
# Return the head of the modified linked list.

# Example 1:

# Input: head = [0,3,1,0,4,5,2,0]
# Output: [4,11]
# Explanation:
# The above figure represents the given linked list. The modified list contains
# - The sum of the nodes marked in green: 3 + 1 = 4.
# - The sum of the nodes marked in red: 4 + 5 + 2 = 11.

# Example 2:

# Input: head = [0,1,0,3,0,2,2,0]
# Output: [1,3,4]
# Explanation:
# The above figure represents the given linked list. The modified list contains
# - The sum of the nodes marked in green: 1 = 1.
# - The sum of the nodes marked in red: 3 = 3.
# - The sum of the nodes marked in yellow: 2 + 2 = 4.

# Constraints:

# The number of nodes in the list is in the range [3, 2 * 105].
# 0 <= Node.val <= 1000
# There are no two consecutive nodes with Node.val == 0.
# The beginning and end of the linked list have Node.val == 0.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Merge all of the nodes in each interval by sum.
        # Each interval is separated by a node with val = 0 -> keep a running sum that resets upon reaching a 0.

        # As we pass each "0" node, replace its value with the current sum.

        sums = []
        dummy = head
        cur_sum = 0

        while head:
            if head.val == 0 and cur_sum != 0:
                sums.append(cur_sum)
                cur_sum = 0
            else:
                cur_sum += head.val
            head = head.next

        head = dummy
        for num_sum in sums:
            head.next = ListNode(num_sum)
            head = head.next

        return dummy.next

# Time Complexity: O(n) -> Traverse the linked list once and re-assign nodes in the list once.
# Space Complexity: O(n) -> Store up to every node once (in case where each interval contains 1 node).