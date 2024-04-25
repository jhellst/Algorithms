# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.
# A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

# Example 1:

# Input: root = [3,4,5,1,2], subRoot = [4,1,2]
# Output: true

# Example 2:

# Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
# Output: false

# Constraints:

# The number of nodes in the root tree is in the range [1, 2000].
# The number of nodes in the subRoot tree is in the range [1, 1000].
# -104 <= root.val <= 104
# -104 <= subRoot.val <= 104


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Find if the tree contains a subtree that == subRoot.

        def dfs(node, subNode):
            if not node and not subNode:
                return True
            elif not node:
                return False
            elif not subNode:
                return False

            if node.val == subNode.val:
                return dfs(node.left, subNode.left) and dfs(node.right, subNode.right)
            else:
                return False


        if not root and not subRoot:
            return True
        elif not root:
            return False
        elif not subRoot:
            return False

        if root.val == subRoot.val:
            if dfs(root, subRoot):
                return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


# Time Complexity: O(n) -> Visit every node in tree, in worst case.
# Space Complexity: O(h) -> O(n) -> Stack may contain a recursive call for every level in the tree.