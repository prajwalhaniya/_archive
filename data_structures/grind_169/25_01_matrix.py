'''
https://leetcode.com/problems/01-matrix/
'''

from collections import deque

class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        if not mat:
            return mat

        m, n = len(mat), len(mat[0])
        queue = deque()
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j))
                else:
                    mat[i][j] = float('inf')

        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            i, j = queue.popleft()
            
            for dx, dy in directions:
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n and mat[x][y] > mat[i][j] + 1:
                    mat[x][y] = mat[i][j] + 1
                    queue.append((x, y))

        return mat
