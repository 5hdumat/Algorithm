# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
import sys
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        low_price = sys.maxsize
        for price in prices:
            low_price = min(price, low_price)
            res = max(res, price - low_price)

        return res

s = Solution()
s.maxProfit([7, 1, 5, 3, 6, 4])
