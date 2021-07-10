# https://leetcode.com/problems/trapping-rain-water/

from typing import List

class Solution:
    # TwoPoiner
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        water_bucket = 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]

        while left < right:
            left_max, right_max = max(left_max, height[left]), max(right_max, height[right])

            if left_max <= right_max:
                water_bucket += left_max - height[left]
                left += 1
            else:
                water_bucket += right_max - height[right]
                right -= 1

        return water_bucket

a = Solution()
a.trap([0,1,0,2,1,0,1,3,2,1,2,1])