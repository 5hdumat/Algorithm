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

        # 시간순 최소힙 구현을 위해 시간, 종점 순으로 출발지 초기화
        Q = [[0, k]]
        dict = collections.defaultdict(list)

        while Q:
            time, node = heapq.heappop(Q)

            # dict는 종점까지의 최단거리 경로이므로 이미 존재한다면 넘어간다.
            if node not in dict:
                dict[node] = time

                for v, w in graph[node]:
                    tmp = time + w
                    heapq.heappush(Q, (tmp, v))

        if len(dict) == n:
            return max(dict.values())

        return -1


s = Solution()
s.networkDelayTime([[3, 1, 5], [3, 2, 2], [2, 1, 2], [3, 4, 1], [4, 5, 1], [5, 6, 1], [6, 7, 1], [7, 8, 1], [8, 1, 1]],
                   8,
                   3)
