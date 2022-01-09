# https://leetcode.com/problems/valid-palindrome/
import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        palindrome = re.sub('[^0-9a-zA-Z]', '', s).lower()
        lp = 0
        rp = len(palindrome) - 1

        while lp < rp:
            if palindrome[lp] == palindrome[rp]:
                lp += 1
                rp -= 1
            else:
                return False
        else:
            return True


s = Solution()
s.isPalindrome("Ab_a")
