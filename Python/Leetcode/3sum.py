# https://leetcode.com/problems/3sum/
from typing import List

class Solution:
    # 브루트 포스 문제풀이
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []

        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            for j in range(i+1, len(nums)-1):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue

                for k in range(j+1, len(nums)):
                    if k > j + 1 and nums[k] == nums[k-1]:
                        continue

                    if nums[i] + nums[j] + nums[k] == 0:
                        output.append([nums[i], nums[j], nums[k]])

        return output

    def threeSumTwoPointer(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []

        print(nums)
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left, right = i+1, len(nums)-1
            while left < right:
                num = nums[i] + nums[left] + nums[right]

                if num < 0:
                    left += 1
                elif num > 0:
                    right -= 1
                else:
                    output.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left+1]:
                        left += 1

                    while left < right and nums[right] == nums[right-1]:
                        right -= 1

                    left += 1
                    right -= 1

        return output

a = Solution()
a.threeSumTwoPointer([0,0,0])