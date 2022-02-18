# https://leetcode.com/problems/merge-intervals/
import collections
import sys
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        results = []

        for x in sorted(intervals):
            if results and results[-1][1] > x[0]:
                results[-1][1] = max(results[-1][1], x[0])
            else:
                results.append(x)

        return results

s = Solution()
s.merge([[2, 3], [1, 7], [3, 6], [8, 10], [15, 18]])
