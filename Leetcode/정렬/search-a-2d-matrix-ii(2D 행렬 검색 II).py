# https://leetcode.com/problems/search-a-2d-matrix-ii/
from typing import List


class Solution:
    def binarySearch(self, lst, target):
        lp, rp = 0, len(lst) - 1

        while lp <= rp:
            mid = (lp + rp) // 2

            if lst[mid] < target:
                lp = mid + 1
            elif lst[mid] > target:
                rp = mid - 1
            else:
                return True

        return False

    def searchMatrix2(self, matrix: List[List[int]], target: int) -> bool:
        lst = []

        for x in matrix:
            lst.extend(x)

        lst.sort()

        return self.binarySearch(lst, target)

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = 0, len(matrix[0]) - 1

        while row < len(matrix) and col >= 0:
            if matrix[row][col] > target:
                col -= 1
            elif matrix[row][col] < target:
                row += 1
            else:
                return True

        return False


s = Solution()
s.searchMatrix([[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 1)
