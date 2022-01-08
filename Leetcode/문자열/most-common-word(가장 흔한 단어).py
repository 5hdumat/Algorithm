# https://leetcode.com/problems/most-common-word/
import collections
import re
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub('[^\w]', ' ', paragraph).lower().split() if not word in banned]
        counter = collections.Counter(words)
        common = counter.most_common(1)

        return common[0][0]


s = Solution()
s.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"])
