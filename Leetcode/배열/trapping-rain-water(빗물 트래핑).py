# https://leetcode.com/problems/trapping-rain-water/
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        bucket = 0
        left = 0
        right = len(height) - 1
        left_max = height[left]
        right_max = height[right]

        while left <= right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])

            if left_max < right_max:
                bucket += left_max - height[left]
                left += 1
            else:
                bucket += right_max - height[right]
                right -= 1

        return bucket

    def trap_stack(self, height: List[int]) -> int:
        bucket = 0
        stack = []

        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                pivot = stack.pop()

                if not stack:
                    break

                distance = i - stack[-1] - 1
                waters = min(height[i], height[stack[-1]]) - height[pivot]

                bucket += distance * waters

            stack.append(i)

        return bucket


s = Solution()
s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
