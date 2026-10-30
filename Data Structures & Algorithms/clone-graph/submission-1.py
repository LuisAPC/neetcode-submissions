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

        original_to_clone = {} # Node : Clone

        def dfs(node: Node) -> Node:
            if node in original_to_clone:
                return original_to_clone[node]

            clone = Node(node.val)
            original_to_clone[node] = clone

            for nei in node.neighbors:
                clone.neighbors.append(dfs(nei))

            return clone

        return dfs(node)
