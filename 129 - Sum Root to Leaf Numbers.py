# You are given the root of a binary tree containing digits from 0 to 9 only.
# Each root-to-leaf path in the tree represents a number.

# For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
# Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

# A leaf node is a node with no children.

# Example 1:

# Input: root = [1,2,3]
# Output: 25
# Explanation:
# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.
# Therefore, sum = 12 + 13 = 25.

# Example 2:

# Input: root = [4,9,0,5,1]
# Output: 1026
# Explanation:
# The root-to-leaf path 4->9->5 represents the number 495.
# The root-to-leaf path 4->9->1 represents the number 491.
# The root-to-leaf path 4->0 represents the number 40.
# Therefore, sum = 495 + 491 + 40 = 1026.

# Constraints:

# The number of nodes in the tree is in the range [1, 1000].
# 0 <= Node.val <= 9
# The depth of the tree will not exceed 10.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # Create numbers as we DFS down each subtree. Numbers are concatenated as strings, and are finally converted to int and added to res when returned.

        def dfs(node, curNum):
            if not node.left and not node.right:
                curNum += str(node.val)
                return int(curNum)

            curNum += str(node.val)
            if not node.left:
                return dfs(node.right, curNum)
            if not node.right:
                return dfs(node.left, curNum)

            return dfs(node.left, curNum) + dfs(node.right, curNum)

        return dfs(root, "")

# Time Complexity: O(n) -> Visit every node 1 time.
# Space Complexity: O(n) -> Stack may contain up to 1 call to dfs for every level of tree (which could be n in worst-case).



# 2nd Solution:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # Starting from the root, sum the "numbers" as denoted from root to leaf.
        # DFS from root node to its leaves -> once we reach a leaf, we can add that total to res.

        self.res = 0
        def dfs(node, cur_val):
            if not node:
                return 0
            cur_val = cur_val * 10 + node.val
            if not node.left and not node.right: # We're at a leaf node -> Add cur_val to res.
                self.res += cur_val
            else:
                dfs(node.left, cur_val)
                dfs(node.right, cur_val)

        dfs(root, 0)
        return self.res

# Time Complexity: O(n) -> Visit every node in binary tree once.
# Space Complexity: O(h) -> O(n) -> Store recursive calls on the stack equal to height of tree. In worst case, h == n.