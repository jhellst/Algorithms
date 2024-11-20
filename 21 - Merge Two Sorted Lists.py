# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.

# Example 1:

# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# Example 2:

# Input: list1 = [], list2 = []
# Output: []

# Example 3:

# Input: list1 = [], list2 = [0]
# Output: [0]

# Constraints:

# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Merge two sorted linked lists together.

        head = ListNode(0, None)
        dummy = head

        while list1 and list2:
            if list1.val <= list2.val:
                head.next = list1
                list1 = list1.next
            else:
                head.next = list2
                list2 = list2.next

            head = head.next

        if list1:
            head.next = list1
        if list2:
            head.next = list2

        return dummy.next

# Time Complexity: O(n + m) -> Visit every node in both linked lists once.
# Space Complexity: O(1) -> No additional storage used.



# 2nd Solution:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 2 sorted lists -> merge them (in order) and return the head of the combined list.

        tail = ListNode(0)
        dummy = tail

        while list1 and list2:
            if list1.val <= list2.val: # list1 has lower val to add.
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        # Now, either both lists are empty or 1 list still contains unvisited nodes. Append the rest of this list (if it exists).
        if list1:
            tail.next = list1
        if list2:
            tail.next = list2

        return dummy.next

# Time Complexity: O(n + m) -> In worst case, visit every node in both lists.
# Space Complexity: O(1) -> No additional storage used.