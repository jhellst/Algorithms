# Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.

# Example 1:

# Input: root = [3,9,20,null,null,15,7]
# Output: [3.00000,14.50000,11.00000]
# Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
# Hence return [3, 14.5, 11].

# Example 2:

# Input: root = [3,9,20,15,7]
# Output: [3.00000,14.50000,11.00000]

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
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # Perform a level-order traversal of the tree, then average the sum of all nodes in the level.

        q = deque()
        q.append(root)
        res = []

        while q:
            q_len = len(q)
            cur_sum = 0
            cur_count = 0
            for _ in range(q_len):
                cur_node = q.popleft()
                if cur_node:
                    q.append(cur_node.left)
                    q.append(cur_node.right)
                    cur_sum += cur_node.val
                    cur_count += 1
            if cur_count:
                res.append(cur_sum / cur_count)

        return res

# Time Complexity: O(n) -> Visit every node of the tree once.
# Space Complexity: O(h) -> O(n) -> Store on deque one node for each level of tree. In worst case, h == n.


# 2nd Solution:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # For each level of the binary tree, append (to res) the average of the values on that level.
        #   - BFS-style traversal -> we'll use a deque and traverse and average, level-by-level.

        res = []
        q = deque([root])

        while q:
            qLen = len(q)
            cur_sum = 0
            for i in range(qLen):
                cur_node = q.popleft()
                if cur_node:
                    cur_sum += cur_node.val
                if cur_node.left:
                    q.append(cur_node.left)
                if cur_node.right:
                    q.append(cur_node.right)

            cur_average = cur_sum / qLen
            res.append(cur_average)

        return res

# Time Complexity: O(n) -> Visit every node in binary tree.
# Space Complexity: O(w) -> O(n) -> Store nodes on deque equal to width of tree. In worst case, w == n.