# Given a binary tree, determine if it is height-balanced.

# Example 1:

# Input: root = [3,9,20,null,null,15,7]
# Output: true

# Example 2:

# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false

# Example 3:

# Input: root = []
# Output: true


# Constraints:

# The number of nodes in the tree is in the range [0, 5000].
# -104 <= Node.val <= 104


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Recursive DFS -> Need to return height of total subtree AND if the subtree is completely balanced internally.

        def dfs(node):
            if not node:
                return [True, 0]

            leftBalance, leftHeight = dfs(node.left)
            rightBalance, rightHeight = dfs(node.right)

            balance = leftBalance and rightBalance and abs(leftHeight - rightHeight) <= 1
            return [balance, max(leftHeight, rightHeight) + 1]

        return dfs(root)[0]

# Time Complexity: O(n) -> Visit every node in the tree once.
# Space Complexity: O(h) -> O(n) -> Stack can contain 1 call for every level in tree, which is every node in worst case.