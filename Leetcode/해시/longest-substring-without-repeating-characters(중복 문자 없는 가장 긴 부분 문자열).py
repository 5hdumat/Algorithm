# https://leetcode.com/problems/longest-substring-without-repeating-characters/
import collections


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        start = res = 0

        for i, v in enumerate(s):
            if v in used and start <= used[v]:
                start = used[v] + 1
            else:
                res = max(res, i - start + 1)

            used[v] = i
            print(used, start)

        return res

    def lengthOfLongestSubstring2(self, s: str) -> int:
        lp = 0
        rp = 1
        res = ''

        while rp <= len(s):
            print(collections.Counter(s[lp:rp]))
            most_common = collections.Counter(s[lp:rp]).most_common()[0][1]

            if most_common == 1:
                res = s[lp:rp]
                rp += 1
            else:
                lp += 1
                rp += 1

        return len('')


s = Solution()
s.lengthOfLongestSubstring2("tmmzmmmzutx")
