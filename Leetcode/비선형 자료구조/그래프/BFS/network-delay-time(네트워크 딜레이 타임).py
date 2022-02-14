# https://leetcode.com/problems/network-delay-time/
import collections
import heapq
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)

        # 목적지, 출발지, 소요시간
        for u, v, w in times:
            graph[u].append((v, w))

        Q = [[0, k]]
        dist = collections.defaultdict(list)

        print(graph)
        while Q:
            time, node = heapq.heappop(Q)

            print(time, node, dist)
            if node not in dist:
                dist[node] = time
                for v, w in graph[node]:
                    tmp = time + w
                    heapq.heappush(Q, [tmp, v])

                print(Q)

        if len(dist) == n:
            return max(dist.values())

        return -1


s = Solution()
s.networkDelayTime([[3, 1, 5], [3, 2, 2], [2, 1, 2], [3, 4, 1], [4, 5, 1], [5, 6, 1], [6, 7, 1], [7, 8, 1], [8, 1, 1]],
                   8,
                   3)
