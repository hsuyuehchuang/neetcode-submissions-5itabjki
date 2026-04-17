class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i : [] for i in range(n)}

        for n1, n2 in edges: # indirected graph
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        visit = set()
        def dfs(n, prev):
            if n in visit:
                return False
            visit.add(n)
            for nei in adj[n]:
                if nei == prev:
                    continue
                dfs(nei, n)
            return True

        res = 0
        for i in range(n):
            if dfs(i, -1):
                res += 1
        return res


# adj []
# visit ()
# dfs
# for i in range(n)
