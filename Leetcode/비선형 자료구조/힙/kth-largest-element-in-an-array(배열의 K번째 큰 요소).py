# https://leetcode.com/problems/kth-largest-element-in-an-array
import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        hq = []

        for x in nums:
            heapq.heappush(hq, -x)

        for _ in range(k):
            res = heapq.heappop(hq) * -1

        return res

    def findKthLargestHeapify(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)

        for _ in range(len(nums) - k):
            heapq.heappop(nums)

        return heapq.heappop(nums)

    def findKthLargestNlargest(self, nums: List[int], k: int) -> int:
        nlargest = heapq.nlargest(k, nums)[-1]

        return nlargest

    def findKthLargestSort(self, nums: List[int], k: int) -> int:
        return sorted(nums, reverse=True)[k - 1]


s = Solution()
s.findKthLargestHeapify([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)
s.findKthLargest([3, 2, 1, 5, 6, 4], 2)
s.findKthLargestNlargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)
s.findKthLargestSort([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)
