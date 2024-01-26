# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

# Example 1:

# Input: root = [3,1,4,null,2], k = 1
# Output: 1

# Example 2:

# Input: root = [5,3,6,2,4,null,null,1], k = 3
# Output: 3


# Constraints:

# The number of nodes in the tree is n.
# 1 <= k <= n <= 104
# 0 <= Node.val <= 104


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Want to find the kth smallest value in the entire tree.
        # Tree is a binary tree, so it is already ordered if we traverse properly (DFS).

        stack = []
        curNode = root
        res = []

        while stack or curNode:
            while curNode: # First, add all nodes going down to the left.
                stack.append(curNode)
                curNode = curNode.left # New curNode is curNode.left (if it exists).
            # Now, done traversing down to the left. Lowest value in tree popped from stack.
            curNode = stack.pop()
            res.append(curNode.val) # Append value to res.
            curNode = curNode.right # Traverse to the right from curNode, if possible.

        return res[k - 1]

# Time Complexity: O(n) -> Single Traversal of tree
# Space Complexity: O(n) -> Single Traversal of tree


# Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?

