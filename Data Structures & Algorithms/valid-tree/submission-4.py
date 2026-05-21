class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        trees = {i: [] for i in range(n)}
        if not n: return True
        for parent, child in edges:
            trees[parent].append(child)
            trees[child].append(parent)

        visit = set()


        def dfs(node, prev):
            
            if node in visit:
                return False
            visit.add(node)

            for i in trees[node]:
                if i == prev:
                    continue
                if not dfs(i, node):
                    return False
                
           
            return True
        return dfs(0, -1)  and len(visit) == n
