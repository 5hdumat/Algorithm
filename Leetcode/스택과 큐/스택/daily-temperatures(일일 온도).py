# https://leetcode.com/problems/daily-temperatures/
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, v in enumerate(temperatures):
            while stack and v > temperatures[stack[-1]]:
                last = stack.pop()
                res[last] = i - last

            stack.append(i)

s = Solution()
s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])
