'''
https://leetcode.com/problems/rotting-oranges/
'''

from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        queue = deque()

        fresh = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
            

        if fresh == 0:
            return 0

        minutes = 0

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue and fresh > 0:
            minutes += 1

            for _ in range(len(queue)):
                x, y = queue.popleft()

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy

                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                        grid[nx][ny] = 2 
                        queue.append((nx, ny))
                        fresh -= 1

        if fresh > 0:
            return - 1

        return minutes