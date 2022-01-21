# https://leetcode.com/problems/daily-temperatures/
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stk = []
        for i, v in enumerate(temperatures):
            while stk and v > temperatures[stk[-1]]:
                last = stk.pop()
                res[last] = i - last

            stk.append(i)

        return res

s = Solution()
s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])
