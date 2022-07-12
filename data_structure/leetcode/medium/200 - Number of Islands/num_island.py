"""
https://leetcode.com/problems/number-of-islands/

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
"""
import collections


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        island = 0
        self.rows, self.cols = len(grid), len(grid[0])

        for r in range(self.rows):
            for c in range(self.cols):
                if grid[r][c] == '1':
                    self.bfs(grid, r, c)
                    island += 1
        return island

    def bfs(self, grid, r, c):
        # initialize a queue
        queue = collections.deque()
        # enqueue the index
        queue.append((r, c))
        # mark it visited or change it to water
        grid[r][c] = '0'

        # loop until queue is not empty
        while queue:
            # dequeue from the queue
            r, c = queue.popleft()
            # spread to all directions and check for adjancent 1.
            directions = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]

            for r, c in directions:
                # make sure not to go beyond the grid.
                if r in range(self.rows) and c in range(self.cols) and grid[r][c] == '1':
                    # enqueue the index
                    queue.append((r, c))
                    # mark it visited or change it to water
                    grid[r][c] = '0'

#     def numIslands(self, grid: List[List[str]]) -> int:
#         if not grid:
#             return 0

#         island = 0
#         self.visit = set()
#         self.rows, self.cols = len(grid), len(grid[0])

#         for r in range(self.rows):
#             for c in range(self.cols):
#                 if grid[r][c] == '1' and (r,c) not in self.visit:
#                     self.bfs(grid, r,c)
#                     island += 1
#         return island

#     def bfs(self, grid, r,c):
#             # intialize a queue
#             queue = collections.deque()
#             # enqueue the index
#             queue.append((r,c))
#             # mark it visited
#             self.visit.add((r,c))

#             while queue:
#                 r, c = queue.popleft()
#                 # spread to all directions and check for 1.
#                 directions = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]

#                 for r, c in directions:
#                     # make sure not to go beyond the grid.
#                     if r in range(self.rows) and c in range(self.cols) and grid[r][c] == '1' and (r,c ) not in self.visit:
#                         # mark it visited
#                         self.visit.add((r,c))
#                         # enqueue the index
#                         queue.append((r,c))





