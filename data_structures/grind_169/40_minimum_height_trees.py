'''
https://leetcode.com/problems/minimum-height-trees/description/
'''
from collections import defaultdict, deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        adj = defaultdict(list)
        
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        leaves = deque()

        for i in range(n):
            if len(adj[i]) == 1:
                leaves.append(i)

        remaining_nodes = n

        while remaining_nodes > 2:
            leaves_size = len(leaves)
            remaining_nodes -= leaves_size
            
            for _ in range(leaves_size):
                leaf = leaves.popleft()
                neighbor = adj[leaf].pop()
                adj[neighbor].remove(leaf)

                if len(adj[neighbor]) == 1:
                    leaves.append(neighbor)

        return list(leaves)

             