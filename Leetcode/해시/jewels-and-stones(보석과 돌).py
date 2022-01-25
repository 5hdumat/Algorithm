# https://leetcode.com/problems/jewels-and-stones/
import collections


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_dict = collections.Counter(stones)
        res = 0

        for jewel in jewels:
            res += jewels_dict[jewel]

        return res


s = Solution()
s.numJewelsInStones("aA", "aAAbbbb")
