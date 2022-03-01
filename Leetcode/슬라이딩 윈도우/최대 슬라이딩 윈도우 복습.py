import collections

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        fast = slow = 0
        window = collections.deque()
        res = []

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
        print(res)
        return res
s = Solution()
s.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3)
s.maxSlidingWindow([1, -1], 1)
s.maxSlidingWindow([7, 2, 4], 2)
