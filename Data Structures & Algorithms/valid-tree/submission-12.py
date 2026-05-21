class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # what is the valid tree
        # a graph with not oop 
        # 0 
        """
        0 

        1    

        2   3 4

        
        """

        adj = {i: [] for i in range(n)}

        for e1, e2 in edges:
            adj[e1].append(e2)
            adj[e2].append(e1)
        visited = set()
        def dfs(previous, node):
            if node in visited:
                return False
            visited.add(node)
            for nextNode in adj[node]:
                if nextNode == previous:
                    continue
                if not dfs(node, nextNode):
                    return False
            return True
        return dfs(-1, 0)  and len(visited) == n



