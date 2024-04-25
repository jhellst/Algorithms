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
        # Use slow and fast pointers to track nodes. Space the pointers out by n+1 nodes. When fast pointer reaches end, slow pointer is right before node to be removed.

        dummy = ListNode(0, head)
        slow, fast = dummy, head

        for i in range(n):
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next

        # Here, slow.next is the node that needs to be removed.
        slow.next = slow.next.next
        return dummy.next

# Time Complexity: O(n) -> Single pass of the array with both pointers.
# Space Complexity: O(1) -> No additional storage.