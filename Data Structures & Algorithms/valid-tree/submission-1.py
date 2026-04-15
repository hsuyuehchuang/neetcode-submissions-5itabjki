class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        
        adj = { i : [] for i in range(n) }
        for v1, v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)
        
        visit = set()
        def dfs(i, prev):
            if i in visit:
                return False
            visit.add(i)
            for nei in adj[i]:
                if nei == prev:
                    continue
                if dfs(nei, i) == False:
                    return False
            return True

        return dfs(0, -1) and n == len(visit)



