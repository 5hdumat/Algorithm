import collections


def solution(n, edges):
    def _dfs(l):
        if len(tmp) == 3:
            print(tmp)
            return

        for x in graph[l]:
            if x not in tmp:
                tmp.append(x)
                _dfs(x)
                tmp.pop()

    graph = collections.defaultdict(list)
    for i, j in edges:
        graph[i].append(j)
        graph[j].append(i)

    tmp = []
    for i in range(n):
        tmp.append(i)
        _dfs(i)
        tmp.pop()


solution(5, [[0, 1], [0, 2], [1, 3], [1, 4]])
