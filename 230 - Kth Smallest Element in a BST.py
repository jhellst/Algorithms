# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

# Example 1:

# Input: root = [3,1,4,null,2], k = 1
# Output: 1

# Example 2:

# Input: root = [5,3,6,2,4,null,null,1], k = 3
# Output: 3


# Constraints:

# The number of nodes in the tree is n.
# 1 <= k <= n <= 104
# 0 <= Node.val <= 104


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # BST, so it can be searched DFS-style and find the Kth element starting from the smallest.
        # At each node, want to process the subtree's nodes by first going to the smallest element (all the way to the left subtree).

        stack = []
        curNode = root
        count = 0

        while stack or curNode:
            while curNode:
                # First phase -> add left leaves, all the way down to bottom row of BST.
                stack.append(curNode)
                curNode = curNode.left

            # We added all possible left subtrees. Current node will NOT need to have its left node added again.
            curNode = stack.pop() # Bottom leaf, currently. Pop it and process into right subtree. Increment k as needed.
            count += 1
            if count == k:
                return curNode.val

            curNode = curNode.right # Go to right subtree now, if it exists.

# Time Complexity: O(n) -> Visit every node in tree, in worst case.
# Space Complexity: O(n) -> Store up to one call on stack for every node in tree (in worst case).


# Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?



# 2nd Solution:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Using the definition of a BST, we can "traverse" the BST to its smallest element before tracking back up, in order.

        stack = []
        cur_node = root
        count = 0

        while cur_node or stack: # Traverse all the way to the far left (smallest element in the subtree).

            while cur_node:
                stack.append(cur_node)
                cur_node = cur_node.left

            cur_node = stack.pop() # cur_node is on top of stack.
            count += 1
            if count == k: # If we're at count == k, return the cur_node's value.
                return cur_node.val

            cur_node = cur_node.right # Step into cur_node's right subtree.

# Time Complexity: O(n) -> In worst case, visit every node in the BST.
# Space Complexity: O(h) -> O(n) -> Store calls on stack for every level of BST. In worst case, h == n.




# 3rd Solution:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Return the kth smallest value.
        #   - We can use the definition of a BST to "traverse" the tree in-order.
        #   - DFS-style traversal is appropriate here.
        # We can travel to the lowest value in the tree (far left node) -> then, we can traverse back upwards.

        count = 0
        stack = []
        cur_node = root

        while cur_node or stack:

            while cur_node: # Traverse to the bottom left leaf of the subtree (smallest value).
                stack.append(cur_node)
                cur_node = cur_node.left
            cur_node = stack.pop() # Pop the lowest value in subtree here.

            # We're at the lowest value in the current subtree.
            count += 1
            if count == k:
                return cur_node.val

            # Now we can traverse to the next lowest value node.
            if cur_node:
                cur_node = cur_node.right

# Time Complexity: O(n) -> In worst case, visit every node in the BST.
# Space Complexity: O(h) -> O(n) -> Store nodes on the stack equal to height of tree. In worst case, h == n.



# 4th Solution:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Iterate through the BST using a stack. Traverse to the lowest value in the BST, storing greater-value nodes on the stack.

        stack = []
        cur_node = root

        while cur_node or stack:
            while cur_node:
                stack.append(cur_node)
                cur_node = cur_node.left
            cur_node = stack.pop() # cur_node is now at lowest (local) value.
            k -= 1
            if k == 0:
                return cur_node.val

            cur_node = cur_node.right # Next greatest node is cur_node.right.

# Time Complexity: O(n) -> Visit each node in BST once.
# Space Complexity: O(h) -> O(n) -> Store nodes on stack up to height of BST. In worst case, h == n.