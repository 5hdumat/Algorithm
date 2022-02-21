# https://leetcode.com/problems/search-in-rotated-sorted-array/
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        # 이진 탐색으로 최솟값 찾기
        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        # 최솟값
        pivot = left

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            mid_pivot = (pivot + mid) % len(nums)

            if nums[mid_pivot] < target:
                left = mid + 1
            elif nums[mid_pivot] > target:
                right = mid - 1
            else:
                return mid_pivot

        return -1


s = Solution()
# s.search([4, 5, 6, 7, 0, 1, 2], 1)
s.search([0, 1, 2, 4, 5, 6, 7], 5)
# s.search([6, 7, 8, 9, 3, 4, 5], 1)
