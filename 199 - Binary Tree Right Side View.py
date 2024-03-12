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
        # We want to see the output of ONLY the right side of the tree. For this reason, we want to take a level-order traversal of the tree.
        # Ensure that the current level is stored -> at end of level, take final number as the "Right Side" view.

        q = deque()
        q.append(root)
        res = []

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
                print(curLevel)
                rightVal = curLevel[-1]
                res.append(rightVal)

        return res

# TIme Complexity: O(n) -> Visit every node in the tree one time.
# Space Complexity: O(d) -> Stack will store, at worst, every node in the final level of the tree. d -> diameter of tree