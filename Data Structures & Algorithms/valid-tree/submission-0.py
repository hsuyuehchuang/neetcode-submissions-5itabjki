class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        
        adj = { i : [] for i in range(n) }
        for n1, n2 in edges:
            adj[n1].append(n2) # 1 -> 2, 1 : 2
            adj[n2].append(n1) # 2 -> 1, 2 : 1
        
        visit = set()
        def dfs(i, prev):
            if i in visit:
                return False
            visit.add(i)
            for nei in adj[i]: # run all neighbors
                if nei == prev: # prev in visit is allowed
                    continue
                if dfs(nei, i) == False:
                    return False
            return True
        
        return dfs(0, -1) and n == len(visit) # -1 is not in the actually initial