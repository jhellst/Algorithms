# Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.
# Return the number of good nodes in the binary tree.

# Example 1:

# Input: root = [3,1,4,3,null,1,5]
# Output: 4
# Explanation: Nodes in blue are good.
# Root Node (3) is always a good node.
# Node 4 -> (3,4) is the maximum value in the path starting from the root.
# Node 5 -> (3,4,5) is the maximum value in the path
# Node 3 -> (3,1,3) is the maximum value in the path.

# Example 2:

# Input: root = [3,3,null,4,2]
# Output: 3
# Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.

# Example 3:

# Input: root = [1]
# Output: 1
# Explanation: Root is considered as good.

# Constraints:

# The number of nodes in the binary tree is in the range [1, 10^5].
# Each node's value is between [-10^4, 10^4].


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # We want to DFS the entire tree. At each node, we want to evaluate if it is a "good" node -> if no nodes from root to node have greater values.

        res = 0
        stack = [[root, root.val]]  # [node, maxVal]

        while stack:
            curNode, curMax = stack.pop()

            if curNode.val >= curMax:
                res += 1
            if curNode.left:
                stack.append([curNode.left, max(curMax, curNode.val)])
            if curNode.right:
                stack.append([curNode.right, max(curMax, curNode.val)])

        return res

# Time Complexity: O(n) -> Visit each node one time.
# Space Complexity: O(n)


# Recursive Solution:

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # Recursive solution. "Good" nodes are nodes that are >= to all parent nodes.

        self.res = 0

        def dfs(node, maxVal):
            if not node:
                return
            if node.val >= maxVal:  # Node.val is valid in chain
                self.res += 1

            dfs(node.left, max(maxVal, node.val))
            dfs(node.right, max(maxVal, node.val))

        dfs(root, root.val)
        return self.res

# Time Complexity: O(n) -> Visit every node in the tree once.
# Space Complexity: O(h) -> O(n) -> Store up to h items on call stack, where h is the height of the tree. In worst case, n = h.


# 2nd Solution:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # Want to count the "good" nodes in the tree.
        #   - A node is "good" if node.val >= all values above it in the tree/subtree.
        # Note: Root node will always be a "good" node.

        # We'll dfs the entire tree, counting "good" nodes along the way.
        # As we step deeper into the tree, ensure that we're adjusting the max_value accordingly.

        def dfs(node, max_value):
            if not node:
                return 0
            if node.val >= max_value:
                return 1 + dfs(node.left, max(node.val, max_value)) + dfs(node.right, max(node.val, max_value))

            return dfs(node.left, max(node.val, max_value)) + dfs(node.right, max(node.val, max_value))

        return dfs(root, root.val)

# Time Complexity: O(n) -> Visit every node in the binary tree once.
# Space Complexity: O(h) -> O(n) -> Store recursive function calls on stack up to height of tree. In worst case, h == n.


# 3rd Solution:


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # Return the total count of "good nodes" -> Nodes that are the greatest value yet seen within the sub-path.
        #   - Determined by their ranking from root -> leaf. (e.g. 3, 4, 5 are all good nodes starting from root)

        # Recursive solution. When we recurse deeper into the tree, must send the info containing the current max_value.
        self.res = 0

        max_val = root.val

        def find_good_nodes(node, max_val):
            if node:
                if node.val >= max_val:  # Check if current node is a good node.
                    self.res += 1
                    max_val = max(max_val, node.val)

                # Now, recurse deeper into the tree to check lower nodes (continue to update max_val as we traverse).
                find_good_nodes(node.left, max_val)
                find_good_nodes(node.right, max_val)

        find_good_nodes(root, max_val)
        return self.res

# Time Complexity: O(n) -> Visit every node once.
# Space Complexity: O(h) -> O(n) -> Recursive calls stored on stack for every level of tree. In worst case, h == n.


# 4th Solution:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # Recursive solution. As we traverse deeper into the tree, the max_val will be re-calculated and passed down.

        def dfs(node, max_val):
            if not node:
                return 0

            if node.val >= max_val:
                return 1 + dfs(node.left, max(max_val, node.val)) + dfs(node.right, max(max_val, node.val))
            return dfs(node.left, max(max_val, node.val)) + dfs(node.right, max(max_val, node.val))

        return dfs(root, root.val)

# Time Complexity: O(n) -> Visit each node once.
# Space Complexity: O(h) -> O(n) -> Store recursive calls on the stack equal to height of tree. In worst case, h == n.
