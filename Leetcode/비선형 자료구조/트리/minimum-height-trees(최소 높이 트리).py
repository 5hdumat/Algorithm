# https://leetcode.com/problems/minimum-height-trees/
import collections
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 1:
            return []

        graph = collections.defaultdict(list)

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        leaves = []
        for x in graph:
            if len(graph[x]) == 1:
                leaves.append(x)

        # 노드가 2개 이상일때만 반복(이 문제의 최단거리 트리 루트는 1개 혹은 2개 일수도 있다.)
        while n > 2:
            n -= len(leaves)
            cur = []

            for leave in leaves:
                pop = graph[leave].pop()
                graph[pop].remove(leave)

                if len(graph[pop]) == 1:
                    cur.append(pop)

            leaves = cur

        return leaves


'''
           x4 - 5x
           |
           3 <- 0x -> 1x
                |
                2x
'''
s = Solution()
s.findMinHeightTrees(6, [[0, 1], [0, 2], [0, 3], [3, 4], [4, 5]])
