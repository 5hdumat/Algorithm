# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
import sys


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res = 0
        for i in range(len(prices) - 1):
            if prices[i] < prices[i + 1]:
                res += prices[i + 1] - prices[i]

        return res
s = Solution()
# s.maxProfit([7, 1, 5, 3, 6, 4])
s.maxProfit([1, 2, 5, 3, 8, 4, 31])
