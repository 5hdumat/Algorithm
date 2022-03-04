# https://leetcode.com/problems/gas-station/
import collections
import heapq


class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas) < sum(cost):
            return -1

        start = tank = 0
        for i in range(len(gas)):
            if gas[i] + tank < cost[i]:
                start = i + 1
                tank = 0
            else:
                tank += gas[i] - cost[i]

        return start


s = Solution()
s.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2])
s.canCompleteCircuit([5, 1, 2, 3, 4], [4, 4, 1, 5, 1])
