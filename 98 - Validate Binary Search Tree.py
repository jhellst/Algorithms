# Given the root of a binary tree, determine if it is a valid binary search tree (BST).
# A valid BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.


# Example 1:

# Input: root = [2,1,3]
# Output: true


# Example 2:

# Input: root = [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.


# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# -231 <= Node.val <= 231 - 1


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # We want to traverse every node in the tree and also ensure that the subtree follows BST logic.
        # Left subtree only contains nodes less than current node.
        # Right subtree only contains nodes greater than current node.

        def checkSubtree(node, left, right): # Checks the subtree and ensures it falls within the BST range of its root.
            if not node:
                return True
            if not (left < node.val < right): # Checks that current node is BST-valid, compared to the higher-level tree.
                return False

            # Check each subtree. Narrow the range that is valid, knowing that node.val needs to be larger than every value in the left subtree and less than every value in the right subtree.
            return checkSubtree(node.left, left, node.val) and checkSubtree(node.right, node.val, right)


        return checkSubtree(root, -inf, inf) # Root node is in range of -inf to inf (any number is valid for root of tree).

# Time Complexity: O(n) -> Checks every node in tree.
# Space Complexity: O(n) -> Stack for recursive calls can include up to 1 call for every node.