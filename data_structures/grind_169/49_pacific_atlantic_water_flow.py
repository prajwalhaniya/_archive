'''
https://leetcode.com/problems/pacific-atlantic-water-flow/
'''
from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []

        rows, cols = len(heights), len(heights[0])
        pacific_reachable = [[False] * cols for _ in range(rows)]
        atlantic_reachable = [[False] * cols for _ in range(rows)]

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def bfs(queue, reachable):
            while queue:
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols:
                        if not reachable[nx][ny] and heights[nx][ny] >= heights[x][y]:
                            reachable[nx][ny] = True
                            queue.append((nx, ny))

        pacific_queue = deque()
        atlantic_queue = deque()

        for i in range(rows):
            pacific_queue.append((i, 0))
            pacific_reachable[i][0] = True
        for j in range(cols):
            pacific_queue.append((0, j))
            pacific_reachable[0][j] = True

        for i in range(rows):
            atlantic_queue.append((i, cols - 1))
            atlantic_reachable[i][cols - 1] = True
        for j in range(cols):
            atlantic_queue.append((rows - 1, j))
            atlantic_reachable[rows - 1][j] = True

        bfs(pacific_queue, pacific_reachable)
        bfs(atlantic_queue, atlantic_reachable)

        
        result = []
        for i in range(rows):
            for j in range(cols):
                if pacific_reachable[i][j] and atlantic_reachable[i][j]:
                    result.append([i, j])

        return result