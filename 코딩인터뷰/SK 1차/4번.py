import collections


def solution(n, edges):
    def _dfs(l):
        if len(tmp) == 3:
            answer.append(tmp[:])
            return

        for x in graph[l]:
            if x not in tmp:
                tmp.append(x)
                _dfs(x)
                tmp.pop()

        return 0

    graph = collections.defaultdict(list)

    for i, j in edges:
        graph[i].append(j)
        graph[j].append(i)

    tmp = []
    answer = []
    for i in range(n):
        tmp.append(i)
        _dfs(i)
        tmp.pop()

    return (len(answer) * 2)


solution(5, [[0, 1], [0, 2], [1, 3], [1, 4]])
solution(4, [[2, 3], [0, 1], [1, 2]])
