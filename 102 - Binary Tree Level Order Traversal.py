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
        # Traverse each level (BFS) and append the level to res array.

        q = deque()
        q.append(root)

        res = []

        # print(q)

        while q:
            qLen = len(q) # Take the length of the queue at the beginning of each new level.
            level = [] # Stores the values for nodes visited on the current level.

            for i in range(qLen): # Pop each node on the current level.
                curNode = q.popleft()
                if curNode:
                    level.append(curNode.val)
                    q.append(curNode.left)
                    q.append(curNode.right)

            if level: # Do not append level if it is an empty array.
                res.append(level)

        return res

# Time Complexity: O(n) -> Traversal of every node in the tree 1 time.
# Space Complexity: O(n) -> Store every node in the tree 1 time.