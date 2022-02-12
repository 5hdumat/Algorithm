# https://leetcode.com/problems/minimum-height-trees/
import collections
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        leaf_node = []
        for x in graph:
            if len(graph[x]) == 1:
                leaf_node.append(x)

        while n > 2:
            n -= len(leaf_node)

            cur = []
            for x in leaf_node:
                parent = graph[x].pop()
                graph[parent].remove(x)

                if len(graph[parent]) == 1:
                    cur.append(parent)

            leaf_node = cur

        return leaf_node
    

'''
           x4 - 5x
           |
           3 <- 0x -> 1x
                |
                2x
'''
s = Solution()
s.findMinHeightTrees(6, [[0, 1], [0, 2], [0, 3], [3, 4], [4, 5]])
