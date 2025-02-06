'''
https://leetcode.com/problems/clone-graph/
'''

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None

        visited = {}

        def dfs(original_node):
            if original_node in visited:
                return visited[original_node]

            clone_node = Node(original_node.val)
            visited[original_node] = clone_node

            for neighbor in original_node.neighbors:
                clone_node.neighbors.append(dfs(neighbor))

            return clone_node

        return dfs(node)