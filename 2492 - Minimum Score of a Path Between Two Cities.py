class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        # Find the minimum score of reaching "n" from position #1.
        # BFS-style solution (or another shortest-path algorithm). Traverse to the end from each node, preventing any cycles by using a set.
        # Note: roads are bi-directional.

        # Idea: We already know that 1 and n are connected.
        #   - Therefore, we can just find the min path that is connected to 1.

        # Traverse the "graph" and return the min_score visited.

        graph = defaultdict(dict) # Allows for double-nested key.

        for u, v, w in roads:
            graph[u][v] = graph[v][u] = w

        min_score = inf
        visited = set()
        queue = deque([1])

        while queue:
            node = queue.popleft()
            for adj, score in graph[node].items():
                print("adj", adj, "score", score)
                if adj not in visited:
                    queue.append(adj)
                    visited.add(adj)
                min_score = min(min_score, score)


        return min_score