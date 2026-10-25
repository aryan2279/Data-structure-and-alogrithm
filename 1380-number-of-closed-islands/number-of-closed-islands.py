class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))

        def flood(sr, sc):
            if grid[sr][sc] != 0:
                return

            stack = [(sr, sc)]
            grid[sr][sc] = 1

            while stack:
                row, col = stack.pop()

                for dr, dc in directions:
                    nr, nc = row + dr, col + dc

                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 0:
                        grid[nr][nc] = 1
                        stack.append((nr, nc))

        for r in range(m):
            flood(r, 0)
            flood(r, n - 1)

        for c in range(n):
            flood(0, c)
            flood(m - 1, c)

        answer = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    answer += 1
                    flood(r, c)

        return answer