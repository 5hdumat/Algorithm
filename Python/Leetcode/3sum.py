# https://leetcode.com/problems/3sum/
from typing import List

class Solution:
    tmp = []
    output = []
    number_list = []

    def dfs(self, depth, idx, visited, nums):
        if depth == 3:
            print(*self.tmp)
            return

        overlap = 0
        for i in range(idx, len(nums)-1):
            if not visited[i] and overlap != self.number_list[i]:
                visited[i] = True

                self.tmp.append(nums[i])
                overlap = self.number_list[i]

                self.dfs(depth + 1, i, visited, nums)

                visited[i] = False
                self.tmp.pop()

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        visited = [False] * len(nums)

        self.dfs(0, 0, visited, nums)

a = Solution()
a.threeSum([-1, 0, 1, 2, -1, -4])