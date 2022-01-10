# https://leetcode.com/problems/array-partition-i/
from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        res = 0

        for i in range(0, len(nums), 2):
            res += nums[i]

        return res


s = Solution()
s.arrayPairSum([1, 4, 3, 2])
