# https://leetcode.com/problems/top-k-frequent-elements/
import collections
import heapq
from typing import List


class Solution:
    def topKFrequentPython(self, nums: List[int], k: int) -> List[int]:
        return list(zip(*collections.Counter(nums).most_common(k)))[0]

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        heap = []
        res = []

        for x in counter.items():
            # 최대 힙을 구해야 하므로 음수 삽입
            heapq.heappush(heap, (-x[1], x[0]))

        for _ in range(k):
            res.append(heapq.heappop(heap)[1])

        return res


s = Solution()
s.topKFrequentPython([1, 1, 1, 2, 2, 2, 2, 3], 2)
