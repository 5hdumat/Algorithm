# https://leetcode.com/problems/largest-number/
from typing import List


class Solution:
    def toSwap(self, e1, e2):
        return e1 + e2 < e2 + e1

    def largestNumber(self, nums: List[int]) -> str:
        nums = sorted(map(str, nums), key=lambda x: x[0], reverse=True)

        for i in range(1, len(nums)):
            j = i
            key = nums[i]

            while j > 0 and self.toSwap(nums[j - 1], key):
                nums[j] = nums[j - 1]
                j -= 1

            nums[j] = key

        return str(int(''.join(nums)))


s = Solution()
s.largestNumber([3, 30, 34, 5, 9])
s.largestNumber([432, 43243])
s.largestNumber([0, 0])
