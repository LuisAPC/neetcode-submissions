# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Recursive DFS
        # if not root:
        #     return 0

        # max_depth = max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        # return max_depth

        # Iterative BFS
        # if not root:
        #     return 0
        
        # depth = 0
        # q = deque([root])
        # while q:
        #     for i in range(len(q)):
        #         node = q.popleft()
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        #     depth += 1
        # return depth

        # Iterative DFS
        stack = [[root, 1]]
        max_depth = 0

        while stack:
            node, depth = stack.pop()
            if node:
                max_depth = max(max_depth, depth)
                stack.append([node.left, depth+1])
                stack.append([node.right, depth+1])
        return max_depth

