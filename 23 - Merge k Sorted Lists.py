# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
# Merge all the linked-lists into one sorted linked-list and return it.

# Example 1:

# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6

# Example 2:

# Input: lists = []
# Output: []

# Example 3:

# Input: lists = [[]]
# Output: []

# Constraints:

#     k == lists.length
#     0 <= k <= 104
#     0 <= lists[i].length <= 500
#     -104 <= lists[i][j] <= 104
#     lists[i] is sorted in ascending order.
#     The sum of lists[i].length will not exceed 104.



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # You have k linked-lists, each sorted in-order. We need to merge them, in-order.
        #   - To do this, we need to take the lowest overall value from the head of each list, until every node has been processed.
        # Solution could use a heap.

        res = []
        d = {i: l for i, l in enumerate(lists)} # Stores [list_num, linked_list]

        tail = ListNode(0)
        dummy = ListNode(0, tail)

        cur_node_heap = [] # Stores [val, list_num] -> Push [val, list] onto heap for each list in lists array.
        for list_num, l in enumerate(lists):
            if l:
                heapq.heappush(cur_node_heap, [l.val, list_num])

        while cur_node_heap: # Take first node from the heap, and add it to tail.

            val_to_add, list_num = heapq.heappop(cur_node_heap)
            node_to_add = d[list_num] # Retrieve the node.

            if node_to_add:
                list_remainder = node_to_add.next
                if list_remainder:
                    d[list_num] = list_remainder
                    heapq.heappush(cur_node_heap, [list_remainder.val, list_num])

                node_to_add.next = None
                tail.next = node_to_add # Add node to end of linked list.
                tail = tail.next # Advance pointer on linked list.

        return dummy.next.next

# Time Complexity: O(n * log(k)) -> Traverse n nodes, and perform heap operations on a heap of length k.
# Space Complexity: 2 * O(k) -> O(k) -> Store k items in a dict, and store k items in a dict.



# 2nd Solution: Merge lists until reduced to a single list.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Given an array of sorted linked lists, merge them, in order.
        # We can combine heap functionality (with mapping) in order to determine the linked list to add from.

        # 2nd Option: Merge 2 lists at a time (in ascending order) until we've merged every list.
        #   - Likely more optimal solution -> it doesn't use heap/sort at any point.

        def merge_2_lists(l1, l2): # Takes 2 sorted arrays and merges them, in order. Returns a single list.
            tail = ListNode()
            dummy = tail

            while l1 and l2:
                if l1.val <= l2.val:
                    tail.next = l1
                    l1 = l1.next
                else:
                    tail.next = l2
                    l2 = l2.next
                tail = tail.next

            if l1:
                tail.next = l1
            if l2:
                tail.next = l2

            return dummy.next

        while len(lists) > 1: # While multiple lists exist, continue to merge them until there is only 1 (sorted) list.
            l1 = lists.pop()
            l2 = lists.pop()
            new_list = merge_2_lists(l1, l2)
            lists.append(new_list)

        if lists and lists[0]:
            return lists[0]

        return

# Time Complexity: O(k * n) -> Merge 2 lists k times. For each merge, we visit n nodes.
# Space Complexity: O(1) -> No additional storage space used.