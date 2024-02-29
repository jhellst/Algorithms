# Given the root of a binary tree, return the length of the longest consecutive sequence path.
# A consecutive sequence path is a path where the values increase by one along the path.
# Note that the path can start at any node in the tree, and you cannot go from a node to its parent in the path.

# Example 1:

# Input: root = [1,null,3,2,4,null,null,null,5]
# Output: 3
# Explanation: Longest consecutive sequence path is 3-4-5, so return 3.

# Example 2:

# Input: root = [2,null,3,2,null,1]
# Output: 2
# Explanation: Longest consecutive sequence path is 2-3, not 3-2-1, so return 2.


# Constraints:

# The number of nodes in the tree is in the range [1, 3 * 104].
# -3 * 104 <= Node.val <= 3 * 104


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        # Find the longest consecutive path -> nodes must increase by 1 along a single path.

        self.maxLength = 1

        def dfs(node):

            if not node:
                return 1

            left = dfs(node.left)
            right = dfs(node.right)

            if node.left:
                if node.left.val - node.val == 1:
                    left += 1
                else:
                    left = 1

            if node.right:
                if node.right.val - node.val != 1:
                    right = 1
                else:
                    right += 1


            self.maxLength = max(self.maxLength, left, right)
            return max(left, right)

        dfs(root)
        return self.maxLength

# Space Complexity: O(n) -> Visit each node once.
# Time Complexity: O(n) -> Recursive, so will store each node on stack in worst case.