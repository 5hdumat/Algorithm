# https://leetcode.com/problems/reorder-data-in-log-files/
from pprint import pprint
from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters = []
        numbers = []
        for x in logs:
            if x.split()[1].isdigit():
                numbers.append(x)
            else:
                letters.append(x)

        # 선순위 식별자로 x[1:] 까지 비교 정렬하되 그 값이 동일하다면 x.split[0]으로 비교
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))

        return letters + numbers


s = Solution()
s.reorderLogFiles(["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"])
