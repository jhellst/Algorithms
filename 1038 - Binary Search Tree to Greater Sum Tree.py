# Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus the sum of all keys greater than the original key in BST.
# As a reminder, a binary search tree is a tree that satisfies these constraints:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

# Example 1:

# Input: root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
# Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]

# Example 2:

# Input: root = [0,null,1]
# Output: [1,null,1]

# Constraints:

# The number of nodes in the tree is in the range [1, 100].
# 0 <= Node.val <= 100
# All the values in the tree are unique.



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        # Traverse the BST from greatest to lowest value -> keep track of a cur_sum value that will start at 0.

        cur_sum = 0
        cur_node = root
        stack = []

        while cur_node or stack:
            while cur_node:
                stack.append(cur_node)
                cur_node = cur_node.right

            cur_node = stack.pop()
            cur_sum += cur_node.val
            cur_node.val = cur_sum

            cur_node = cur_node.left

        return root

# Time Complexity: O(n) -> Visit every node in the tree once.
# Space Complexity: O(h) -> O(n) -> Store 1 node on the stack for each level of the tree. In worst case, h == n.