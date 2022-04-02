# https://leetcode.com/problems/permutations/
import itertools
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ch = [0] * len(nums)
        tmp = []
        res = []

        def _dfs(l):
            if l == len(nums):
                res.append(tmp[:])
                return res

            for i in range(len(nums)):
                if ch[i] == 0:
                    ch[i] = 1
                    tmp.append(nums[i])

                    _dfs(l + 1)

                    ch[i] = 0
                    tmp.pop()

        _dfs(0)

        print(res)
        return res

    def permute2(self, nums: List[int]) -> List[List[int]]:
        results = []
        prev = []

        def dfs(elements):
            if len(elements) == 0:
                results.append(prev[:])
                return

            for e in elements:
                tmp = elements[:]
                tmp.remove(e)
                prev.append(e)

                dfs(tmp)
                prev.pop()

        dfs(nums)

        print(results)
        return results

    def permute3(self, nums: List[int]) -> List[List[int]]:
        return list(map(list, itertools.permutations(nums)))


s = Solution()
s.permute3([1, 2, 3])
