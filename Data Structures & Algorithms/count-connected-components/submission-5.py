class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # 0  
        # 1 
        # 2
        # 3    4  5

        graph = {i: [] for i in range(n)}
        
        for e1, e2 in edges:
            graph[e1].append(e2)
            graph[e2].append(e1)

        visited = set()
        count = 0
        def dfs(node):
            if node in visited:
                return 
            visited.add(node)
            for nextNode in graph[node]:
                dfs(nextNode)
            
            return
        
        for node in graph.keys():
            if node not in visited:
                count += 1
                dfs(node)
        return count