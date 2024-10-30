# You are given the head of a singly linked-list. The list can be represented as:

# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:

# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.


# Example 1:

# Input: head = [1,2,3,4]
# Output: [1,4,2,3]


# Example 2:

# Input: head = [1,2,3,4,5]
# Output: [1,5,2,4,3]


# Constraints:

# The number of nodes in the list is in the range [1, 5 * 104].
# 1 <= Node.val <= 1000

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Want to take a linked list and reorder in the following pattern:
        #       first, last, second, second to last, ...


        # 1) Split the list in half.
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # Fast is at end of list and slow is one node before the halfway point. Split after the slow node.
        # Also need to make slow.next = None to split the list.
        second = slow.next
        slow.next = None

        # 2) Reverse the 2nd half of the list.
        prev = None

        while second:
            nextNode = second.next # Store next node to advance to later.
            second.next = prev # Make current second.next = prev node.

            prev = second # Set prev = current node.
            second = nextNode # Advance current node.

        # At end of this sequence, prev will be first node in the 2nd half (already reversed) list.
        first, second = head, prev

        # 3) Zipper-style merge of the two lists.
        while first and second:
            tmp1, tmp2 = first.next, second.next
            first.next, second = second, tmp1
            first = first.next


# Time Complexity: O(n) -> Traverse list to split (O(n)), and Traverse split lists to link (O(n)).
# Space Complexity: O(n) -> No additional storage.




# 2nd Solution:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # We want to reorder the list in the following way:
        #   - Split the list in half, then zipper-merge the two lists with the 2nd list reversed.
        # Return the head of the resulting linked list that is joined.

        dummy = ListNode(0, head)
        # First, we want to "split" the list into 2 parts.
        #   - Use fast, slow pointers to split the list.

        slow, fast = dummy, dummy
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Now, fast == None and slow is located on the last node of L1. Split them now (start of L2 is slow.next).
        l2 = slow.next
        slow.next = None
        # The lists are split. L1's head == head and L2's head == l2.

        # Reverse the 2nd list and return its head afterwards.
        prev = None
        while l2:
            tmp = l2.next
            l2.next = prev

            prev = l2
            l2 = tmp
        # prev is head of L2 (after reversing).

        # Now, zipper-merge the two lists (starting with l1's head as 1st node).
        l1, l2 = head, prev
        while l1 and l2: # L1 will be >= in length to L2.
            tmp_1, tmp_2 = l1.next, l2.next
            l1.next = l2

            l2 = tmp_1
            l1 = l1.next

        return head

# Time Complexity: O(n) -> 2 complete traversals of linked list of length n.
# Space Complexity: O(1) -> No additional storage used.