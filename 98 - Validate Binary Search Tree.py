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



# 2nd Solution:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Need to traverse the entire BST while validating each value. Recursive definition is simple implementation here.
        #   - When we step into left subtree, maxVal reduces.
        #   - When we step into right subtree, minVal increases.

        def dfs(node, minVal, maxVal):
            if not node:
                return True
            elif node.val <= minVal or node.val >= maxVal:
                return False
            return dfs(node.left, minVal, min(maxVal, node.val)) and dfs(node.right, max(minVal, node.val), maxVal)


        return dfs(root, -inf, inf) # Start at root, with all numbers valid initially. Range will narrow as we step into each subtree.

# Time Complexity: O(n) -> In worst case, visit every node in tree once.
# Space Complexity: O(h) -> O(n) -> Call stack may include a function call for every level of the tree. In worst case, h == n.





# 3rd Solution:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Recursively visit each node, determining if it is "valid" based on basic BST definition.
        #   - Left value (if node exists) must be lower than entirety of above range.
        #   - Right value (if node exists) must be higher than entirety of above range.

        def is_valid_subtree(node, min_val, max_val):
            if not node:
                return True
            if node.val <= min_val or node.val >= max_val:
                return False
            # Recurse into subnodes -> reset min/max range when calling function.
            #   - Left -> Reduce max_val
            #   - Right -> Increase min_val
            return is_valid_subtree(node.left, min_val, min(max_val, node.val)) and is_valid_subtree(node.right, max(min_val, node.val), max_val)

        return is_valid_subtree(root, -inf, inf)

# Time Complexity: O(n) -> In worst case, visit each node once.
# Space Complexity: O(h) -> O(n) -> Store recursive calls on the stack equal to height of the tree. In worst case, h == n.