# You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.
# Return the number of connected components in the graph.

# Example 1:


# Input: n = 5, edges = [[0,1],[1,2],[3,4]]
# Output: 2

# Example 2:

# Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
# Output: 1

# Constraints:

# 1 <= n <= 2000
# 1 <= edges.length <= 5000
# edges[i].length == 2
# 0 <= ai <= bi < n
# ai != bi
# There are no repeated edges.



class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Unclear description of problem. Appears that we are trying to find the number of separate connected groups of nodes.

        # Create adjacency list for later DFS.
        adj = {}
        visited = set() # To store visited nodes when counting "islands".

        for node, nextNode in edges:
            if node in adj:
                adj[node].append(nextNode)
            else:
                adj[node] = [nextNode]

            if nextNode in adj:
                adj[nextNode].append(node)
            else:
                adj[nextNode] = [node]


        def dfs(node):
            if node not in visited: # Once the node is visited, we don't want to visit it again.
                visited.add(node)
                connectedNodes = adj.get(node, [])
                for nextNode in connectedNodes:
                    dfs(nextNode)

        count = 0

        # Traverse nodes and dfs for "islands".
        for node in range(n):
            if node not in visited:
                count += 1
                dfs(node)
            if nextNode not in visited:
                count += 1
                dfs(nextNode)

        return count

# Time Complexity: O(e + v) -> visit each vertex, DFS visits every edge in each vertex.
# Space Complexity: O(e + v)