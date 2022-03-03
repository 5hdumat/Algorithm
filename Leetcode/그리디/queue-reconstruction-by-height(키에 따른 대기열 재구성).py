# https://leetcode.com/problems/queue-reconstruction-by-height/
import collections
import heapq


class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        heap = []

        for x in people:
            heapq.heappush(heap, (-x[0], x[1]))

        while heap:
            pop = heapq.heappop(heap)

            res.insert(pop[1], [-pop[0], pop[1]])

        return res


s = Solution()
s.reconstructQueue([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]])
