# https://leetcode.com/problems/climbing-stairs/
import collections


class Solution(object):
    dp = collections.defaultdict(int)

    def climbStairs(self, n):
        if n <= 2:
            return n

        if self.dp[n]:
            return self.dp[n]

        self.dp[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)

        return self.dp[n]

s = Solution()
s.climbStairs(6)

'''
          3

        2   1

     1  0  0  -1
   
   0  -1 
   
0 지점이 계단 도착 경우의 수 (피보나치 수열과 동일)

0 1 1 2 3 5 8 13
'''
