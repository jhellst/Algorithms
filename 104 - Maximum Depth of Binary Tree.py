# Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Example 1:

# Input: root = [3,9,20,null,null,15,7]
# Output: 3

# Example 2:

# Input: root = [1,null,2]
# Output: 2

# Constraints:

# The number of nodes in the tree is in the range [0, 104].
# -100 <= Node.val <= 100



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Recursive definition is easiest to implement.

        def dfs(root):
            if not root:
                return 0

            # Non-terminating case, return max depth of both subtrees.
            left = dfs(root.left)
            right = dfs(root.right)
            return 1 + max(left, right)

        return dfs(root)

# Time Complexity: O(n) -> Visit every node in the tree once.
# Space Complexity: O(n) -> Stack will contain # of calls equal to height of tree, which COULD be n.