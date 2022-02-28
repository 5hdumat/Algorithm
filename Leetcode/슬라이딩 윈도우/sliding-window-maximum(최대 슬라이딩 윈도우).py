# https://leetcode.com/problems/sliding-window-maximum/
import collections
import sys


class Solution(object):
    # 런너 활용
    def maxSlidingWindow(self, nums, k):
        res = []
        window = collections.deque()
        fast = slow = 0

        while fast < len(nums):
            while window and window[-1] < nums[fast]:
                window.pop()
            window.append(nums[fast])

            if fast - slow + 1 == k:
                res.append(window[0])

                if window[0] == nums[slow]:
                    window.popleft()
                slow += 1

            fast += 1
        return res

    # 타임아웃 발생
    def maxSlidingWindowTimeout(self, nums, k):
        result = []
        window = collections.deque()
        max_size = -sys.maxsize

        for i, v in enumerate(nums):
            window.append(v)

            if i < k - 1:
                continue

            if max_size == -sys.maxsize:
                max_size = max(window)
            elif max_size < v:
                max_size = v

            result.append(max_size)

            if max_size == window.popleft():
                max_size = -sys.maxsize

        return result

    # 타임아웃 발생
    def maxSlidingWindowTimeout2(self, nums, k):
        res = []
        for i in range(0, len(nums) - k + 1):
            res.append(max(nums[i:k + i]))

        return res


s = Solution()
# s.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3)
s.maxSlidingWindow([1, -1], 1)
