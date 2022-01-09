# https://leetcode.com/problems/two-sum/
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}

        for i, n in enumerate(nums):
            nums_map[n] = i

        for i, n in enumerate(nums):
            # target - n in nums_map: (딕셔너리에 존재하지 않는 키를 조회하면 keyError가 발생하므로 예외처리)
            # i != nums_map[target - n]: target - n의 값이 n과 동일하면 n의 인덱스가 그대로 반환되므로 예외처리 [테스트 케이스: s.twoSum([3, 2, 4], 6)]
            if target - n in nums_map and i != nums_map[target - n]:
                print([i, nums_map[target - n]])
                return [i, nums_map[target - n]]

    # 성능 차이는 없지만 간결한 코드로 개선
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}

        for i, n in enumerate(nums):
            if target - n in nums_map:
                print(nums_map[target - n], i)
            nums_map[n] = i


s = Solution()
s.twoSum2([3, 2, 4], 6)
