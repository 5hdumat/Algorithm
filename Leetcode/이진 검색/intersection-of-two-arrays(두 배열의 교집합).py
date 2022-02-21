# https://leetcode.com/problems/intersection-of-two-arrays/
import bisect
from typing import List


class Solution:
    def binarySearch(self, nums, target):
        left, right = 0, len(nums) - 1

        while left <= right:

            mid = (left + right) // 2

            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return nums[mid]

        return -1

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums = sorted((set(nums1)))

        res = []
        for x in set(nums2):
            search = self.binarySearch(nums, x)
            if search != -1:
                res.append(search)

        return res

    def intersection2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = set()
        nums2.sort()

        for x in nums1:
            search = bisect.bisect_left(nums2, x)

            if 0 < len(nums2) and search < len(nums2) and x == nums2[search]:
                res.add(x)

        return res


s = Solution()
s.intersection2([1, 2, 2, 1], [2, 2])
s.intersection2([4, 9, 5], [9, 4, 9, 8, 4])
