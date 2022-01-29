# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        def _dfs(index):
            if len(tmp) == len(digits):
                res.append(''.join(tmp))
                return

            for i in range(index, len(digits)):
                for x in graph[digits[i]]:
                    tmp.append(x)
                    _dfs(i + 1)
                    tmp.pop()

        graph = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        res = []
        tmp = []

        _dfs(0)
        return res


s = Solution()
s.letterCombinations("")
