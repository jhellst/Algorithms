# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Recursive DFS-style traversal of the binary tree. At each point, we want to 1) calculate the max path at current node and compare to res and 2) return the max length of left/right side only.

        self.res = 0

        def dfs(node):
            if not node:
                return 0
            left =  dfs(node.left)
            right =  dfs(node.right)

            self.res = max(self.res, left + right)
            return 1 + max(left, right)

        dfs(root)
        return self.res

# Time Complexity: O(n) -> Visit every node 1 time.
# Space Complexity: Recursive calls on stack, up to 1 for every node in worst case.