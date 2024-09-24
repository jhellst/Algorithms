# You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.
# Return true if the edges of the given graph make up a valid tree, and false otherwise.

# Example 1:

# Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
# Output: true

# Example 2:

# Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
# Output: false

# Constraints:

#     1 <= n <= 2000
#     0 <= edges.length <= 5000
#     edges[i].length == 2
#     0 <= ai, bi < n
#     ai != bi
#     There are no self-loops or repeated edges.



class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # A tree is valid if, and only if, nodes have (at most) 1 parent.
        # Use a set to store nodes that we've already seen. If we see the same node again, we can return False.
        # Traverse the tree, either BFS or DFS, and store nodes in set for later reference.

        adj_list = defaultdict(set)

        for start, end in edges:
            adj_list[start].add(end)
            adj_list[end].add(start)

        seen = set()
        q = deque([0])

        while q:
            cur_node = q.popleft()
            if cur_node in seen:
                return False
            seen.add(cur_node)

            for child_node in adj_list[cur_node]:
                adj_list[child_node].remove(cur_node)
                q.append(child_node)

        return len(seen) == n

# Time Complexity: O(n) -> Visit every node in the tree.
# Space Complexity: O(w) -> O(n) -> Store recursive calls equal to width of the tree. In worst case, w == n.