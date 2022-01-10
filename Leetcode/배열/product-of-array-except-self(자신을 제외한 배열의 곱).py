# https://leetcode.com/problems/product-of-array-except-self/
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []

        # 일단 마지막 요소를 제외한 나머지 항목의 곱을 구한다.
        # [1, 1, 2, 6]
        p = 1
        for i in range(len(nums)):
            res.append(p)
            p = p * nums[i]

        # [1, 1, 2, 6]
        # [24, 12, 4, 1]
        p = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] = res[i] * p
            p = p * nums[i]

        return res


s = Solution()
s.productExceptSelf([1, 2, 3, 4])
