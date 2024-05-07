# You are given the head of a non-empty linked list representing a non-negative integer without leading zeroes.
# Return the head of the linked list after doubling it.

# Example 1:

# Input: head = [1,8,9]
# Output: [3,7,8]
# Explanation: The figure above corresponds to the given linked list which represents the number 189. Hence, the returned linked list represents the number 189 * 2 = 378.

# Example 2:

# Input: head = [9,9,9]
# Output: [1,9,9,8]
# Explanation: The figure above corresponds to the given linked list which represents the number 999. Hence, the returned linked list reprersents the number 999 * 2 = 1998.

# Constraints:

# The number of nodes in the list is in the range [1, 104]
# 0 <= Node.val <= 9
# The input is generated such that the list represents a number that does not have leading zeros, except the number 0 itself.





# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Reverse the linked list. Then traverse it while doubling each number. Ensure that a placeholder is maintained.

        tail = head
        prev = None

        while tail:
            nxt = tail.next
            tail.next = prev
            prev = tail
            tail = nxt

        # Now, we have the list reversed. Start to re-process, while storing placeholders and also re-reversing the list.

        tail = prev
        remainder = 0
        prev = None

        while tail:
            nxt = tail.next
            tail.next = prev

            curValue = tail.val * 2 + remainder
            curDigit, remainder = curValue % 10, curValue // 10
            tail.val = curDigit

            prev = tail
            tail = nxt

        # If we still have a remainder, we need to add another node.
        if remainder:
            return ListNode(remainder, prev)

        return prev

# Time Complexity: O(n) -> Traverse a linked list and reverse it twice.
# Space Complexity: O(1) -> No additional storage used.