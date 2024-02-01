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
        # BFS-style traversal of binary tree.
        # Want to traverse, level-by-level, and append each complete level to res.

        res = []

        q = deque()
        q.append(root)

        while q:
            qLen = len(q) # Take the length of the current level.
            curLevel = []
            for i in range(qLen): # Pop each node on the current level.
                cur = q.popleft()
                if cur:
                    curLevel.append(cur.val)
                    q.append(cur.left)
                    q.append(cur.right)

            if curLevel: # Only append to res if values are included.
                res.append(curLevel)

        return res

# Time Complexity: O(n) -> Traversal of every node in the tree 1 time.
# Space Complexity: O(n) -> Store every node in the tree 1 time.