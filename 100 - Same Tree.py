# Given the roots of two binary trees p and q, write a function to check if they are the same or not.
# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

# Example 1:

# Input: p = [1,2,3], q = [1,2,3]
# Output: true

# Example 2:

# Input: p = [1,2], q = [1,null,2]
# Output: false
# Example 3:

# Input: p = [1,2,1], q = [1,1,2]
# Output: false

# Constraints:

# The number of nodes in both trees is in the range [0, 100].
# -104 <= Node.val <= 104


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Need to traverse each subtree AND determine that the nodes are equal values for each tree.

        if not p and not q:
            return True
        elif not p:
            return False
        elif not q:
            return False

        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# Time Complexity: O(n) -> Must visit every node in each tree once.
# Space Complexity: O(h) -> O(n) -> Store recursive calls on the stack, up to height of the tree.



# 2nd Solution:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Return True if the trees are identical, otherwise return False.

        if not p and not q:
            return True
        elif not p or not q:
            return False
        elif p.val != q.val:
            return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# Time Complexity: O(n) -> In worst case, visit every node in both trees.
# Space Complexity: O(h) -> O(n) -> Store recursive calls on the stack up to height of tree. In worst case, h == n.