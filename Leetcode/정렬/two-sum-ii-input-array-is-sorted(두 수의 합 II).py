# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lp = 0
        rp = len(numbers) - 1
        res = []
        while lp < rp:
            sum = numbers[lp] + numbers[rp]
            if sum > target:
                rp -= 1
            elif sum < target:
                lp += 1
            else:
                res.append([lp + 1, rp + 1])
                lp += 1
                rp -= 1

        return res

    def twoSumBinarySearch(self, numbers: List[int], target: int) -> List[int]:
        for k, v in enumerate(numbers):
            # 본인을 제외한 나머지 탐색
            lp, rp = k + 1, len(numbers) - 1
            target_v = target - v

            while lp <= rp:
                mid = (lp + rp) // 2

                if numbers[mid] < target_v:
                    lp = mid + 1
                elif numbers[mid] > target_v:
                    rp = mid - 1
                else:
                    return k + 1, mid + 1


s = Solution()
s.twoSum([2, 7, 11, 15], 9)
s.twoSumBinarySearch([2, 7, 11, 15], 9)
s.twoSum([1, 2, 3, 4], 6)
