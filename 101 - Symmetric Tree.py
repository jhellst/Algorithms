# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

# Example 1:
# Input: root = [1,2,2,3,4,4,3]
# Output: true

# Example 2:
# Input: root = [1,2,2,null,3,null,3]
# Output: false

# Constraints:
#     The number of nodes in the tree is in the range [1, 1000].
#     -100 <= Node.val <= 100

# Follow up: Could you solve it both recursively and iteratively?



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # Check whether or not a binary tree is symmetrical and return True if so, False otherwise.
        #   - We want to "traverse" with 2 separate sides simulateously, while comparing.

        if not root:
            return True

        def dfs(left_subtree, right_subtree):
            if not left_subtree and not right_subtree:
                return True
            elif not left_subtree or not right_subtree:
                return False
            elif left_subtree.val == right_subtree.val:
                return dfs(left_subtree.left, right_subtree.right) and dfs(left_subtree.right, right_subtree.left)
            else:
                return False

        return dfs(root.left, root.right)

# Time Complexity: O(n) -> In worst case, visit each node in binary tree one time.
# Space Complexity: O(h) -> O(n) -> Store recursive calls on the stack up to height of tree. In worst case, h == n.