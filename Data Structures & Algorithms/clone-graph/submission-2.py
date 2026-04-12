"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}

        if node in oldToNew:
            return oldToNew[node]

        copy = Node(node.val) # copy the value first
        oldToNew[node] = copy

        def dfs(node):
            for nei in node.neighbors:
                nei_copy = dfs(nei)
                copy.neighbors.append(nei_copy)
            return copy
    
        return dfs(node)




