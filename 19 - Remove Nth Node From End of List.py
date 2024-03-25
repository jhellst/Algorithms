# Given the head of a linked list, remove the nth node from the end of the list and return its head.


# Example 1:


# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Example 2:

# Input: head = [1], n = 1
# Output: []
# Example 3:

# Input: head = [1,2], n = 1
# Output: [1]


# Constraints:

# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Want to remove nth node from the end of the list. We can achieve this by setting slow and fast pointers.
        # Have the fast pointer move n # of nodes from the beginning before the slow pointer. When fast pointer reaches the end, slow pointer will be just before the node to be removed. Remove the node by making node.next => node.next.next instead.

        dummy = ListNode(0, head)
        slow = dummy
        fast = head

        for i in range(n):
            fast = fast.next

        # Now, fast is n nodes ahead of slow.

        while fast:
            slow = slow.next
            fast = fast.next

        # Now slow.next is the node that will be skipped.
        slow.next = slow.next.next

        return dummy.next


# Time Complexity O(n) -> Single pass
# Space Complexity O(1) -> No additional storage used
