# https://leetcode.com/problems/house-robber/
import collections


class Solution(object):
    def rob(self, nums):
        if not nums:
            return 0

        if len(nums) <= 3:
            return max(nums)

        dp = collections.OrderedDict()

        dp[0], dp[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[i]

s = Solution()
# s.rob([1, 2, 3, 1])
# s.rob([2, 7, 9, 3, 1])
# s.rob([2, 7, 9, 3, 1])
s.rob([8, 7, 3, 1, 12, 14, 13, 9])
# s.rob([2, 12, 9, 3, 1])
# s.rob([2, 1, 1, 2])
# s.rob([1, 2, 3, 1])
