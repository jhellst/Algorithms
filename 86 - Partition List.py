# Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
# You should preserve the original relative order of the nodes in each of the two partitions.

# Example 1:

# Input: head = [1,4,3,2,5,2], x = 3
# Output: [1,2,2,4,3,5]

# Example 2:

# Input: head = [2,1], x = 2
# Output: [1,2]

# Constraints:
#     The number of nodes in the list is in the range [0, 200].
#     -100 <= Node.val <= 100
#     -200 <= x <= 200



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # Traverse the linked list and append into 2 separate linked lists -> 1) before and 2) after.
        #   - Process each node and add to before/after, depending on value.
        #   - Finally, link before and after together and return the head.

        before, after = ListNode(0), ListNode(0)
        before_dummy, after_dummy = before, after

        while head:
            nxt = head.next

            if head and head.val < x: # Move to "before" list.
                before.next = head
                head.next = None
                before = before.next
            else: # Move to "after" list.
                after.next = head
                head.next = None
                after = after.next

            head = nxt

        # Now, we have each list ordered properly. We just have to link these.
        #   - We have the final node of "before" list -> append first node of "after" list and then return before_dummy.next.

        before.next = after_dummy.next
        return before_dummy.next

# Time Complexity: O(n) -> Traverse linked list once.
# Space Complexity: O(1) -> No additional storage used.