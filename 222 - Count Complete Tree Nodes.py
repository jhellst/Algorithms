# Given the root of a complete binary tree, return the number of the nodes in the tree.
# According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.
# Design an algorithm that runs in less than O(n) time complexity.

# Example 1:

# Input: root = [1,2,3,4,5,6]
# Output: 6

# Example 2:

# Input: root = []
# Output: 0

# Example 3:

# Input: root = [1]
# Output: 1

# Constraints:

#     The number of nodes in the tree is in the range [0, 5 * 104].
#     0 <= Node.val <= 5 * 104
#     The tree is guaranteed to be complete.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # Traverse each node of the tree, incrementing res
        # Definition of complete binary tree -> tree will be balanced and all rows are filled (besides the last).
        #   - Using this definition, we can easily determine if we're on the next-to-last level of the tree.
        #       -> If any node in this level does not have 2 nodes, we're at the last node.

        node_count = 0

        stack = [root]
        while stack:
            cur_node = stack.pop()
            if cur_node:
                node_count += 1
                stack.append(cur_node.left)
                stack.append(cur_node.right)

        return node_count

# Time Complexity: O(n) -> Visit every node in the binary tree once.
# Space Complexity: O(log(n)) -> Store log(n) nodes on stack.


# Solution 2:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # Count the number of nodes in the binary tree and return it.
        # Recursive solution -> DFS-style traversal to reach (and count) every node.

        def dfs(node):
            if not node:
                return 0
            return 1 + dfs(node.left) + dfs(node.right)

        return dfs(root)

# Time Complexity: O(n) -> Visit every node in the binary tree once.
# Space Complexity: O(h) -> O(n) -> Store recursive calls on the stack. In worst case, h == n.
