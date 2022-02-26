# https://leetcode.com/problems/number-of-1-bits/

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        # print(bin(0b1011), 0b1011)
        # print(bin(0b1011 & 0b1011 - 1), 0b1011 & 0b1011 - 1)
        # print(bin(0b1010 & 0b1010 - 1), 0b1010 & 0b1010 - 1)
        # print(bin(0b1000 & 0b1000 - 1), 0b1000 & 0b1000 - 1)
        count = 0
        while n:
            n &= n - 1
            count += 1

        return count


s = Solution()
s.hammingWeight(0b00000000000000000000000010000000)
