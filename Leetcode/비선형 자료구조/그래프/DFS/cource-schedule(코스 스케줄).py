import collections
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def _dfs(s):
            if s in traced:
                return False

            # 이미 방문한 곳은 순환구조임을 검증하지 않아도 된다.
            if s in visited:
                return True

            traced.add(s)

            for y in graph[s]:
                if not _dfs(y):
                    return False

            traced.remove(s)
            visited.add(s)

            return True

        graph = collections.defaultdict(list)

        for a, b in prerequisites:
            graph[a].append(b)

        traced = set()
        visited = set()
        for x in list(graph):
            if not _dfs(x):
                return False

        return True


s = Solution()
finish = s.canFinish(2, [[1, 0], [0, 1]])
print(finish)
