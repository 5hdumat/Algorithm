# https://leetcode.com/problems/majority-element/
import collections
from typing import List


class Solution(object):
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return None

        if len(nums) == 1:
            return nums[0]

        center = len(nums) // 2
        a = self.majorityElement(nums[:center])
        b = self.majorityElement(nums[center:])

        # a와 b는 nums 배열에서 과반수 데이터만 재귀적으로 반환한다.
        # 분할 정복이후 조합이 진행되면서 모든 배열이 합쳐지고 추려진 과반수 데이터(a, b)의 대소 관계를 또 판별한다.
        # return [b, a][nums.count(a) > center]
        print(a, b, nums, [a, b][nums.count(a) < center])
        return [a, b][nums.count(a) <= center]

    # 메모이제이션 활용
    def majorityElementDP(self, nums: List[int]) -> int:
        counts = collections.defaultdict(int)
        for num in nums:
            if counts[num] == 0:
                counts[num] = nums.count(num)

            if counts[num] > len(nums) // 2:
                return num


s = Solution()
# print(s.majorityElement([2, 2, 3, 3, 3, 1, 1, 1, 2, 2, 3, 3]))
print(s.majorityElement([6, 5, 5]))
# dp = s.majorityElementDP([2, 2, 3, 3, 3, 1, 1, 1, 2, 2, 3, 3])
