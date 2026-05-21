class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i: [] for i in range(n)}

        for e1, e2 in edges:
            adj[e1].append(e2)
            adj[e2].append(e1)

        visit = set()
        count = 0
        def dfs(node):
            if node in visit:
                return False
           
            visit.add(node)
            
            for nextNode in adj[node]:
                dfs(nextNode)
            return True
        
         
        for i in range(n):
            if dfs(i):
                count += 1
        return count