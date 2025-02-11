# Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

# Example 1:
# Input: root = [4,2,6,1,3]
# Output: 1

# Example 2:
# Input: root = [1,0,48,null,null,12,49]
# Output: 1

# Constraints:
#     The number of nodes in the tree is in the range [2, 104].
#     0 <= Node.val <= 105


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # Traverse the BST and calculate the difference between each value.

        self.min_diff = inf
        self.val_set = set() # Contains every value included.

        def traverse(node):
            if node:
                for val in self.val_set:
                    cur_diff = abs(node.val - val)
                    self.min_diff = min(self.min_diff, cur_diff)
                self.val_set.add(node.val)
                traverse(node.left)
                traverse(node.right)

        traverse(root)
        return self.min_diff