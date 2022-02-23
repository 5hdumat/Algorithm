# https://leetcode.com/problems/single-number/

class Solution(object):
    def singleNumber(self, nums):
        result = 0

        for num in nums:
            result ^= num

        return result


s = Solution()
# s.singleNumber([2, 2, 1])
s.singleNumber([4, 1, 2, 1, 2])
