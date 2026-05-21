class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # every edgfes must be connected and there is no loop
        if not edges: return True
        visited = set()
        adj = {i: [] for i in range(n)}
        for e1, e2 in edges:
            adj[e1].append(e2)
            adj[e2].append(e1)
        
        def dfs(node, prev):
            if node in visited:
                return False
            visited.add(node)

            for nextNode in adj[node]:
                if nextNode == prev:
                    continue
                if not dfs(nextNode, node):
                    return False
            return True
        
        result = dfs(0, float("-inf"))
        return result and len(visited) == n
