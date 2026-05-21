class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # there is no loop and all node must be visited 

        if not edges: return True

        # we have to connect the edges
        adj = {i : [] for i in range(n)}

        for e1, e2 in edges:
            adj[e1].append(e2)
            adj[e2].append(e1)
        # so now we have a graph to check if it is a tree
        visited = set()
        def dfs(node, prev):
      
            if node in visited:
                return False
            visited.add(node)

            for i in (adj[node]):
                if i == prev:
                    continue
                if not dfs(i, node):
                    return False
            return True
        return dfs(0, -1) and len(visited) == n 