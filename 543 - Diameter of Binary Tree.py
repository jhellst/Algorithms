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
            left = dfs(node.left)
            right = dfs(node.right)

            self.res = max(self.res, left + right)
            return 1 + max(left, right)

        dfs(root)
        return self.res

# Time Complexity: O(n) -> Visit every node 1 time.
# Space Complexity: Recursive calls on stack, up to 1 for every node in worst case.


# 2nd Solution:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Return the max diameter of the tree (length of any connected nodes).
        # DFS-style traversal -> at each node, we'll re-process res AND pass the max_length from other paths into the recursive call.

        self.max_length = 0

        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            self.max_length = max(self.max_length, left + right)
            return 1 + max(left, right)

        dfs(root)
        return self.max_length
