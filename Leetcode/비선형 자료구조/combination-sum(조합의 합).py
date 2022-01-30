# https://leetcode.com/problems/combination-sum/
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(target, s):
            if target < 0:
                return

            if target == 0:
                res.append(tmp[:])
                return

            for i in range(s, len(candidates)):
                tmp.append(candidates[i])
                dfs(target - candidates[i], i)
                tmp.pop()

        if 0 in candidates:
            return []

        tmp = []
        res = []
        dfs(target, 0)

        return res

s = Solution()
s.combinationSum([0, 2, 3, 6, 7], 8)
