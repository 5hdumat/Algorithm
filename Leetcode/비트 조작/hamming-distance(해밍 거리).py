# https://leetcode.com/problems/hamming-distance

class Solution(object):
    def hammingDistance(self, x, y):
        return bin(x ^ y).count('1')

s = Solution()
s.hammingDistance(1, 4)
