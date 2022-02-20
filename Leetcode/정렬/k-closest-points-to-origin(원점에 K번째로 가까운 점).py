# https://leetcode.com/problems/k-closest-points-to-origin/
import collections
import heapq
import math
from typing import List


class Solution:

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for point in points:
            heapq.heappush(heap, (math.sqrt((0 - point[0]) ** 2, (0 - point[1]) ** 2), point))

        res = []
        while heap and k:
            pop = heapq.heappop(heap)
            res.append(pop[1])
            k -= 1

        return res


s = Solution()
s.kClosest([[1, 3], [-2, 2]], 1)
s.kClosest([[3, 3], [5, -1], [-2, 4]], 2)
s.kClosest([[1, 3], [-2, 2], [2, -2]], 2)
