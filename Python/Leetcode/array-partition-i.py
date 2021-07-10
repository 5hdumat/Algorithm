# https://leetcode.com/problems/array-partition-i/
from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        output = 0
        pair = []
        nums.sort()

        for i in nums:
            pair.append(i)

            if len(pair) == 2:
                output += min(pair)

                pair = []

        return output

    def arrayPairSum2(self, nums: List[int]) -> int:
        output = 0
        nums.sort()

        for i in range(0, len(nums)-1, 2):
            output += nums[i]

        return output

    def arrayPairSum3(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])

a = Solution()
a. arrayPairSum3([1, 4, 3, 2])