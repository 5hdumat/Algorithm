# https://leetcode.com/problems/3sum/
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        print(nums)
        # pivot 인덱스를 기준으로 오른쪽 데이터에 투포인터를 잡는다.
        for pivot in range(len(nums) - 2):
            if pivot > 0 and nums[pivot] == nums[pivot - 1]:
                continue

            left = pivot + 1
            right = len(nums) - 1
            while left < right:
                sum = nums[pivot] + nums[left] + nums[right]

                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    res.append([nums[pivot], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

        return res


s = Solution()
s.threeSum([-1, 0, 1, 2, -1, -1])
