# https://leetcode.com/problems/maximum-subarray/
import collections
import sys


class Solution(object):
    def maxSubArray(self, nums):
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1] if nums[i - 1] > 0 else 0

        return max(nums)

    def maxSubArrayKadane(self, nums):
        prev = 0
        maximum = -sys.maxsize
        for num in nums:
            prev = max(num, prev + num)
            maximum = max(maximum, prev)

        return maximum


s = Solution()
# s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
s.maxSubArrayKadane([-2, 1, -3, 4, -1, 2, 1, -5, 4])
