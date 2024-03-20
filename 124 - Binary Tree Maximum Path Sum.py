# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.
# The path sum of a path is the sum of the node's values in the path.
# Given the root of a binary tree, return the maximum path sum of any non-empty path.

# Example 1:

# Input: root = [1,2,3]
# Output: 6
# Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

# Example 2:

# Input: root = [-10,9,20,null,null,15,7]
# Output: 42
# Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.

# Constraints:

# The number of nodes in the tree is in the range [1, 3 * 104].
# -1000 <= Node.val <= 1000

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        # DFS of each subtree. When we reach a new node, we evaluate maxPath AND also return value of max path (left or right) + node.val.
        # Key Takeaway: At each point, we want to calculate between max of left, right, and both. BUT we want to return max of left/right to the DFS.
        maxPath = root.val

        def dfs(root):
            nonlocal maxPath

            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)

            curPathSum = root.val + max(left, 0) + max(right, 0) # Max path at current node.
            maxPath = max(maxPath, curPathSum) # Compare against maxPath.

            return root.val + max (left, right, 0) # Return max path of either left + root or right + root

        dfs(root)
        return maxPath

# Time Complexity: O(n) -> DFS of each node once
# Space Complexity: O(n) -> Store up to every node on the stack.