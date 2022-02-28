# https://leetcode.com/problems/minimum-window-substring/
import collections


class Solution(object):
    # 슬라이딩 윈도우 + 투포인터 결합
    def minWindow(self, s, t):
        left = start = end = 0
        window = collections.Counter(t)
        missing = len(t)
        for right, char in enumerate(s, 1):
            missing -= window[char] > 0
            window[char] -= 1

            if missing == 0:
                while left < right and window[s[left]] < 0:
                    window[s[left]] += 1
                    left += 1

                # end가 0이거나 이전 윈도우 범위가 현재 윈도우 범위보다 크거나 같을 때 left 증가(윈도우 범위 좁히기)
                if not end or right - left <= end - start:
                    start, end = left, right
                    window[s[left]] += 1
                    left += 1
                    missing += 1

        return s[start: end]


s = Solution()
s.minWindow("ADOBECODEBANC", "ABC")
