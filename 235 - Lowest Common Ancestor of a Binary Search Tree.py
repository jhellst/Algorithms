# Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.
# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

# Example 1:

# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
# Output: 6
# Explanation: The LCA of nodes 2 and 8 is 6.

# Example 2:

# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
# Output: 2
# Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

# Example 3:

# Input: root = [2,1], p = 2, q = 1
# Output: 2


# Constraints:

# The number of nodes in the tree is in the range [2, 105].
# -109 <= Node.val <= 109
# All Node.val are unique.
# p != q
# p and q will exist in the BST.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Need to find LCA -> closest ancestor that has both p and q as descendants (# or the node itself).
        # Value is a binary search tree, which is a key insight.

        # Key takeaway: if p.val and q.val are on opposite sides of the tree, then we are at the LCA.

        cur = root
        while cur:
            if p.val < cur.val and q.val < cur.val: # Both vals are on left side of tree.
                cur = cur.left
            elif p.val > cur.val and q.val > cur.val: # Both vals are on right side of tree.
                cur = cur.right
            else:
                # This captures every other case where p.val and q.val aren't on the same side of tree.
                # This scenario captures:
                #   1) root is equal to p or q -> this is the LCA.
                #   2) p and q are on opposites sides of cur -> this is the LCA.
                return cur

# Time Complexity: O(log(n)) -> Traverse the tree, binary search-like.
# Space Complexity: O(1) -> No additional storage needed.


# 2nd Solution -> Recursive.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # LCA is the node that has both p and q as descendants (or self).
        # We want to recursively search down the tree until either
        #   1) We're at p or q, and p or q is "downstream"
        #   2) Both p and q are "downstream" in separate sides of the tree.
        # BST -> Therefore, we can search towards the right direction.

        def recurse(node):
            if node.val > p.val and node.val < q.val: # Values are in left/right subtrees.
                return node
            elif node.val == p.val or node.val == q.val:
                return node
            elif node.val > p.val and node.val > q.val: # Both values are in left subtree.
                return recurse(node.left)
            elif node.val < q.val and node.val < p.val: # Both values are in right subtree.
                return recurse(node.right)

            return node # Return root of tree, if we reach this point.

        return recurse(root)

# Time Complexity: O(n) -> Traverse the entirety of the BST in worst case.
# Space Complexity: O(h) -> O(n) -> Store recursive calls on the stack equal to h. In worst case, h == n.