# Given the root of a binary tree, invert the tree, and return its root.

# Example 1:

# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]

# Example 2:

# Input: root = [2,1,3]
# Output: [2,3,1]

# Example 3:

# Input: root = []
# Output: []

# Constraints:

# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Reverse all of the subtrees (left and right should be swapped).

        def reverse(node):
            if not node:
                return None
            else:
                left = reverse(node.left)
                right = reverse(node.right)
                node.left, node.right = right, left
                return node

        return reverse(root)

# Time Complexity: O(n) -> Visit every node in tree exactly 1 time.
# Space Complexity: O(h) -> Call stack can contain up to h calls (where h is height of tree).


# 2nd Solution:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Invert the entire binary tree. EVERY subtree will be reversed beneath the root, and then the root is returned.

        if not root:
            return None

        left = self.invertTree(root.left) if root.left else None
        right = self.invertTree(root.right) if root.right else None

        # Reverse the subtrees.
        root.left, root.right = right, left

        return root

# Time Complexity: O(n) -> Visit (and reverse) every node in the binary tree exactly once.
# Space Complexity: O(h) -> O(n) -> Call stack contains one call for each level in the tree -> In worst case, h == n.