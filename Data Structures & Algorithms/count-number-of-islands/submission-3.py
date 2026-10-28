class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # O(n2)

        # 1. BFS
        # from collections import deque
        
        # if not grid:
        #     return 0

        # islands = 0
        # visited = set()
        # rows = len(grid)
        # cols = len(grid[0])


        # def bfs(r: str, c: str) -> None:
        #     q = deque([(r, c)])
        #     visited.add((r, c))
        #     directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        #     while q:
        #         cur_r, cur_c = q.popleft()

        #         for dr, dc in directions:
        #             nr = cur_r + dr
        #             nc = cur_c + dc

        #             if (0 <= nr < rows and
        #                 0 <= nc < cols and
        #                 (nr, nc) not in visited and
        #                 grid[nr][nc] == "1"):
        #                 q.append((nr, nc))
        #                 visited.add((nr, nc))


        # for r in range(rows):
        #     for c in range(cols):
        #         if grid[r][c] == "1" and (r, c) not in visited:
        #             bfs(r, c)
        #             islands += 1
        # return islands

        # 2. DFS
        # And not using visited set
        if not grid:
            return 0

        islands = 0
        rows = len(grid)
        cols = len(grid[0])


        def dfs(r: str, c: str) -> None:
            if (r < 0 or
                r >= rows or
                c < 0 or
                c >= cols or
                grid[r][c] != "1"):
                return

            grid[r][c] = "0"

            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(r, c)
                    islands += 1
        return islands
