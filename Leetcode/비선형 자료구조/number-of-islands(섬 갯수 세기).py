# https://leetcode.com/problems/number-of-islands/
from typing import List


class Solution:
    grid: List[List[str]]

    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid = grid

        def _dfs(x, y):
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] != '1':
                return

            grid[x][y] = 0

            for i in range(4):
                tx = x + dx[i]
                ty = y + dy[i]

                _dfs(tx, ty)

        res = 0
        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    _dfs(i, j)
                    res += 1

        return res


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

s = Solution()
s.numIslands(
    [["1", "1", "1"], ["0", "1", "0"], ["1", "1", "1"]])

# class Solution:
#     def dfs(self, x, y, grid):
#         for i in range(4):
#             tx = x + dx[i]
#             ty = y + dy[i]
#
#             if grid[tx][ty] == 1:
#                 grid[tx][ty] = 0
#                 self.dfs(tx, ty, grid)
#
#         return 1
#
#     def numIslands(self, grid: List[List[str]]) -> int:
#         res = 0
#         m, n = len(grid), len(grid[0])
#
#         for i in range(m):
#             for j in range(n):
#                 grid[i][j] = int(grid[i][j])
#
#         grid.insert(0, [0] * n)
#         grid.append([0] * n)
#
#         for i in range(m + 2):
#             grid[i].insert(0, 0)
#             grid[i].append(0)
#
#         for i in range(m + 2):
#             for j in range(n + 2):
#                 if grid[i][j] == 1:
#                     grid[i][j] = 0
#                     res += self.dfs(i, j, grid)
#
#         return res
#
#
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]
