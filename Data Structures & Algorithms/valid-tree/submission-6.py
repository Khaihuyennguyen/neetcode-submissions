class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n: return True

        # check if there is any loop or in another word
        # if the node is visit => return False
        adj = {i: [] for i in range(n)}

        for e1, e2 in edges:
            adj[e1].append(e2)
            adj[e2].append(e1)
        visit = set()

        def dfs(node, prev):
            if node in visit:
                return False
            visit.add(node)

            for nextNode in adj[node]:
                if nextNode == prev:
                    continue
                if not dfs(nextNode, node):
                    return False
            return True
        return dfs(0, -1) and len(visit) == n # avoid disconnent component


            