# https://leetcode.com/problems/longest-palindromic-substring/
import math

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left: int, right: int) -> str:
            print(left, right)
            print('---------')
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                
                print(left, right)
                print(s[left + 1:right])
                print('===========')
                
            return s[left + 1:right]
            
        result = ''
        for i in range(len(s)):
            result = max(result, expand(i, i+1), expand(i, i+2), key=len)
            
a = Solution()
a.longestPalindrome("123454321")