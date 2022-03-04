# https://leetcode.com/problems/assign-cookies/
import bisect
from collections import deque


class Solution(object):
    def findContentChildren(self, child, cookies):
        child.sort()
        cookies.sort()

        child_i = cookie_j = 0
        while child_i < len(child) and cookie_j < len(cookies):
            if child[child_i] <= cookies[cookie_j]:
                # print(child[child_i], cookies[cookie_j])
                child_i += 1
            cookie_j += 1

        return child_i

    def findContentChildrenBinary(self, child, cookies):
        child.sort()
        cookies.sort()

        result = 0
        for cookie in cookies:
            index = bisect.bisect_right(child, cookie)
            if index > result:
                result += 1

        return result


s = Solution()
# s.findContentChildren([1, 2, 3], [1, 1])
# s.findContentChildrenBinary([1, 2], [1, 2, 3])
# s.findContentChildren([1, 2, 3], [])
# s.findContentChildren([1, 2], [1, 2, 3])
# s.findContentChildren([10, 9, 8, 7], [5, 6, 7, 8])
s.findContentChildrenBinary([10, 9, 8, 7], [5, 6, 7, 8])
# 7 8 9 10 / 5 6 7 8