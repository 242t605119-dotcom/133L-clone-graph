"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node):
        if not node:
            return None

        copies = {}

        def dfs(node):
            if node in copies:
                return copies[node]

            copies[node] = Node(node.val)

            for neighbor in node.neighbors:
                copies[node].neighbors.append(dfs(neighbor))

            return copies[node]

        return dfs(node)
