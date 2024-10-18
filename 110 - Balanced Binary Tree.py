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



# 2nd Solution:


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Height difference of > 1 makes the entire tree NOT balanced.
        # DFS into each subtree, returning the maxLength of the subtree AND a boolean that determines if the subtree itself is balanced.

        def dfs(node):
            if not node:
                return [True, 0]

            left = dfs(node.left) # [Boolean, max_subtree_height]
            right = dfs(node.right) # [Boolean, max_subtree_height]

            if left[0] and right[0] and abs(left[1] - right[1]) <= 1: # If both subtrees are balanced AND the height difference is no more than 1 -> return [True, max_height + 1].
                return [True, 1 + max(left[1], right[1])]

            return [False, 0]

        return dfs(root)[0]

# Time Complexity: O(n) -> Visit every node in the BST in worst case.
# Space Complexity: O(h) -> O(n) -> Call stack contains recursive function calls for every level of the tree. In worst case, h == n.


# 3rd Solution:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Return True/False to determine if the tree is high-balanced.
        #   - Height-balanced: For any node, no 2 subtrees differ in height by more than 1.

        # Solution can be recursive -> check each subtree as we traverse lower into the tree.

        def dfs(node):
            if not node:
                return [True, 0] # [is_balanced, height]

            # Now, we need to determine the balance between the two current subtrees.
            left_is_balanced, left_height = dfs(node.left)
            right_is_balanced, right_height = dfs(node.right)
            left_height += 1
            right_height += 1

            # Determine if 1) nested subtrees are balanced and 2) that current subtrees are balanced (within 1 height).
            is_balanced = left_is_balanced and right_is_balanced and abs(left_height - right_height) <= 1
            subtree_height = max(left_height, right_height)

            return [is_balanced, subtree_height]

        return dfs(root)[0]