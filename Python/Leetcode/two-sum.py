# https://leetcode.com/problems/two-sum/

# 브루트포스 문제풀이 (O(n^2)) :: 4140 ms
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        
a = Solution()
a.twoSum([3, 2, 4], 6)

#  in 이용 문제풀이 (O(n^2)) :: 656 ms
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            tmp = target - n
            
            if tmp in nums[i+1:]:
                return [nums.index(n), nums[i + 1:].index(tmp) + (i + 1)]
        
a = Solution()
a.twoSum([3, 3], 6)

#  in 이용 성능 개선 문제풀이 (O(n))
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            complement = target - n
            
            if complement in nums[i+1:]:
                return [nums.index(n), nums[i + 1:].index(complement) + (i + 1)]
        
a = Solution()
a.twoSum([3, 3], 6)

#  in 이용 성능 개선 문제풀이 (O(n)) :: 64 ms
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i, n in enumerate(nums):
            num_map[n] = i
        
        for i, n in enumerate(nums):
            # dictionary의 in은 키에 한해서 동작합니다.
            if target - n in num_map and i != num_map[target - n]:
                return [i, num_map[target - n]]
            
a = Solution()
a.twoSum([3, 3], 6)

#  in 이용 코드 스타일 개선 문제풀이 (O(n)) :: 64 ms
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i, n in enumerate(nums):
            if target - n in num_map:
                return [num_map[target - n], i]

            num_map[n] = i
            
a = Solution()
a.twoSum([3, 2, 4], 6)
