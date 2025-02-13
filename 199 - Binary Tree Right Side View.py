# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

# Example 1:

# Input: root = [1,2,3,null,5,null,4]
# Output: [1,3,4]

# Example 2:

# Input: root = [1,null,3]
# Output: [1,3]

# Example 3:

# Input: root = []
# Output: []

# Constraints:

# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Output should contain the far right value of each level, when traversing level-by-level.
        # Use a BFS-style traversal while tracking the # of nodes in each level. At the end of each level, append the final value in that level's array.

        res = []

        q = deque()
        q.append(root)

        while q:
            qLen = len(q)
            curLevel = []

            for _ in range(qLen):
                curNode = q.popleft()
                if curNode:
                    curLevel.append(curNode.val)
                    q.append(curNode.left)
                    q.append(curNode.right)

            if curLevel:
                res.append(curLevel[-1])

        return res

# Time Complexity: O(n) -> Visit every node exactly 1 time.
# Space Complexity: O(w) -> curLevel array used to store each node on a current level.



# 2nd Solution:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Level-order traversal -> After each level is "collected" append the final item stored on the queue for that level.
        # Use a deque.

        q = deque()
        q.append(root)
        res = []

        while q:
            qlen = len(q)
            cur_level = []
            for i in range(qlen):
                cur_node = q.popleft()
                if cur_node:
                    cur_level.append(cur_node.val)
                    q.append(cur_node.left)
                    q.append(cur_node.right)

            if cur_level:
                res.append(cur_level[-1])

        return res

# Time Complexity: O(n) -> Visit every node in binary tree.
# Space Complexity: O(h) -> O(n) -> Store nodes on deque equal to height of tree. In worst case, h == n.