# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).


# Example 1:

# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]

# Example 2:

# Input: root = [1]
# Output: [[1]]
# Example 3:

# Input: root = []
# Output: []


# Constraints:

# The number of nodes in the tree is in the range [0, 2000].
# -1000 <= Node.val <= 1000


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Level-order traversal of tree. Use deque to traverse and append each level.

        res = []
        q = deque()
        q.append(root)

        while q:
            qLen = len(q)
            curLevel = []
            for i in range(qLen):
                curNode = q.popleft()
                if curNode:
                    curLevel.append(curNode.val)
                    q.append(curNode.left)
                    q.append(curNode.right)

            if curLevel:
                res.append(curLevel)

        return res

# Time Complexity: O(n) -> Visit every node in the tree exactly 1 time.
# Space Complexity: O(w) -> O(n) -> Store up to w nodes on the stack, where w is the width of any given level of the tree.



# 2nd Solution:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Return the level-order traversal of the nodes values.
        #   - BFS-style traversal (iterative using a deque). Keep track of the entire level, and append it.

        res = []
        q = deque()
        q.append(root)

        while q:
            q_len = len(q)
            cur_level = []

            for i in range(q_len):
                cur_node = q.popleft()
                if cur_node:
                    cur_level.append(cur_node.val)
                    q.append(cur_node.left)
                    q.append(cur_node.right)
            if cur_level:
                res.append(cur_level)

        return res

# Time Complexity: O(n) -> Visit every node in the binary tree once.
# Space Complexity: O(w) -> O(n) -> Store nodes on deque up to size of current level of the tree. In worst case, w == n.