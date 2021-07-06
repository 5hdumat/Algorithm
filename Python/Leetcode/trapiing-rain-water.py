# https://leetcode.com/problems/trapping-rain-water/

from typing import List

class Solution:
    def trapTwoPoiner(self, height: List[int]) -> int:
        water_bucket = 0
        left, right = 0, len(height) - 1
        left_point, right_point = height[left], height[right]
        
        while left < right:
            left_point, right_point = max(left_point, height[left]),  max(right_point, height[right])
            
            if left_point <= right_point:
                water_bucket += left_point - height[left]
                left += 1
                
            else:
                water_bucket += right_point - height[right]  
                right -= 1
                
        return water_bucket          
        
a = Solution()
a.trapTwoPoiner([0,1,0,2,1,0,1,3,2,1,2,1])