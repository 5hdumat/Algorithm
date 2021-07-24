# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
import sys
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = sys.maxsize

        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)

        return profit

a = Solution()
a.maxProfit([7, 1, 5, 3, 6, 4])