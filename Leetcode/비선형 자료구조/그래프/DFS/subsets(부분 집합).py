# https://leetcode.com/problems/subsets/
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def _dfs(l, s):
            res.append(tmp[:])

            for i in range(s, len(nums)):
                if ch[i] == 0:
                    ch[i] = 1
                    tmp.append(nums[i])

                    _dfs(l + 1, i)

                    ch[i] = 0
                    tmp.pop()

        tmp = []
        ch = [0] * (len(nums) + 1)
        res = []
        _dfs(0, 0)

        print(res)
        return res


s = Solution()
s.subsets([0, 1, 2])
