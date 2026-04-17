class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)] # empty list of list, more efficient than dict

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visit = set()
        def dfs(node):
            if node in visit:
                return False
            visit.add(node)
            for nei in adj[node]:
                dfs(nei)
            return True

        res = 0
        for i in range(n):
            if i not in visit:
                dfs(i)
                res += 1
        return res