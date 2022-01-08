# https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(pl, pr):
            while pl >= 0 and pr < len(s) and s[pl] == s[pr]:
                pl -= 1
                pr += 1

            return s[pl + 1:pr]

        if len(s) < 2 or s == s[::-1]:
            return s

        result = ''
        for i in range(len(s)):
            result = max(result,
                         expand(i, i + 1),
                         expand(i, i + 2),
                         key=len)

        return result


s = Solution()
s.longestPalindrome("babaababababbd")
