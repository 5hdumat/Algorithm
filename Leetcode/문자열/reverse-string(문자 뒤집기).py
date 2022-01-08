# https://leetcode.com/problems/reverse-string/
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        lp = 0
        rp = len(s) - 1

        while lp < rp:
            s[lp], s[rp] = s[rp], s[lp]
            lp += 1
            rp -= 1

        print(s)


s = Solution()

if __name__ == '__main__':
    s.reverseString(["h","e","l","l","o"])
