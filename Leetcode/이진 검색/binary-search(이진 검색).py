# https://leetcode.com/problems/binary-search/
import bisect
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lp = 0
        rp = len(nums) - 1

        while lp <= rp:
            pivot = (lp + rp) // 2

            if nums[pivot] == target:
                return pivot

            if nums[pivot] < target:
                lp = pivot + 1

            else:
                rp = pivot - 1

        return -1

    def searchPython(self, nums: List[int], target: int) -> int:
        index = bisect.bisect_left(nums, target)

        if index < len(nums) and nums[index] == target:
            return index
        else:
            return -1


s = Solution()
s.search([-1, 0, 3, 5, 9, 12], 9)
s.search([5], 5)
