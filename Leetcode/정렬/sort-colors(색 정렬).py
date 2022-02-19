# https://leetcode.com/problems/sort-colors/
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        for i in range(1, len(nums)):
            j = i
            key = nums[i]

            while j > 0 and nums[j - 1] > key:
                nums[j] = nums[j - 1]
                j -= 1

            nums[j] = key

        return nums


s = Solution()
colors = s.sortColors([2, 0, 2, 1, 1, 0])
