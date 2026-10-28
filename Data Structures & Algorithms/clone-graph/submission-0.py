"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return

        old_to_new = {} # old node : new node

        def dfs(node: Optional['Node']) -> Optional['Node']:
            if node in old_to_new:
                return old_to_new[node]

            clone = Node(node.val)
            old_to_new[node] = clone
            for n in node.neighbors:
                clone.neighbors.append(dfs(n))
            return clone

        return dfs(node)