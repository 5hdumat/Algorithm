# https://leetcode.com/problems/combinations/
import itertools
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(l, s):
            if l == k:
                res.append(tmp[:])
                return

            for i in range(s, n + 1):
                if ch[i] == 0:
                    ch[i] = 1
                    tmp.append(i)
                    dfs(l + 1, i + 1)

                    ch[i] = 0
                    tmp.pop()

        ch = [0] * (n + 1)
        tmp = []
        res = []
        dfs(0, 1)

        return res

    def combine_python(self, n: int, k: int) -> List[List[int]]:
        return list(itertools.combinations(range(1, n + 1), k))


s = Solution()
s.combine_python(4, 2)
