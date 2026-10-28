class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        rows = len(grid)
        cols = len(grid[0])
        visited = set()

        if not grid:
            return islands

        def bfs(r: str, c: str) -> None:
            q = deque([(r, c)])
            visited.add((r, c))
            directions = [[1,0], [-1, 0], [0, 1], [0, -1]]
            while q:
                cur_r, cur_c = q.popleft()
                for dr, dc in directions:
                    new_r, new_c = dr + cur_r, dc + cur_c
                    if (new_r in range(rows) and
                        new_c in range(cols) and 
                        (new_r, new_c) not in visited and
                        grid[new_r][new_c] == "1"):
                        visited.add((new_r, new_c))
                        q.append((new_r, new_c))

        
        for r in range(rows):
            for c in range(cols):
                if (grid[r][c] == "1" and
                    (r, c) not in visited):
                    bfs(r, c)
                    islands += 1
        return islands
