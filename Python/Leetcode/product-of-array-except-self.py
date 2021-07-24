# https://leetcode.com/problems/product-of-array-except-self/
from typing import List

class Solution:
    def productExceptSelf2(self, nums: List[int]) -> List[int]:
        output = []

        n = 1
        left, right = [], []

        for i in range(0, len(nums)):
            left.append(n)
            n *= nums[i]

        n = 1
        for i in range(len(nums), 0, -1):
            right.append(n)
            n *= nums[i-1]

        for i in range(0, len(nums)):
            output.append(left[i] * right[len(nums)-1 - i])

        return output

    # 코드개선
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        output = []

        # 왼쪽 곱셈
        for i in range(0, len(nums)):
            output.append(p)
            p *= nums[i]

        # 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈
        p = 1
        for i in range(len(nums), 0, -1):
            output[i-1] *= p
            p *= nums[i-1]

        return output

a = Solution()
a.productExceptSelf([1,2,3,4])