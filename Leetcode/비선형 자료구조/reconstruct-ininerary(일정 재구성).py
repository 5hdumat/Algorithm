# https://leetcode.com/problems/reconstruct-itinerary/
import collections
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def _dfs(s):
            while graph[s]:
                pop = graph[s].pop()
                _dfs(pop)

            res.append(s)

        graph = collections.defaultdict(list)

        for s, d in sorted(tickets, reverse=True):
            graph[s].append(d)

        res = []
        _dfs('JFK')

        return res[::-1]

    def findItineraryStack(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        for s, d in sorted(tickets, reverse=True):
            graph[s].append(d)

        print(graph)
        route, stack = [], ['JFK']
        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop())

            route.append(stack.pop())

        print(route[::-1])

s = Solution()
s.findItineraryStack([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]])
