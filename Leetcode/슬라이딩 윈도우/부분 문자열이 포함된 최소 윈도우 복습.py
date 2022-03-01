import collections


class Solution(object):
    # 슬라이딩 윈도우 + 투포인터 결합
    def minWindow(self, s, t):
        left = start = end = 0
        graph = collections.Counter(t)
        missing = len(t)

        for right, char in enumerate(s, 1):
            missing -= graph[char] > 0
            graph[char] -= 1

            if missing == 0:
                while left < right and graph[s[left]] < 0:
                    graph[s[left]] += 1
                    left += 1

                if not end or right - left <= end - start:
                    start, end = left, right
                    graph[s[left]] += 1
                    left += 1
                    missing += 1

        return s[start:end]


s = Solution()
s.minWindow("ADOBECODEBANC", "ABC")
