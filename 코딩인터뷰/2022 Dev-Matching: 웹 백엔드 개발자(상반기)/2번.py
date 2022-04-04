from collections import deque
from copy import deepcopy
from itertools import product


def solution(grid):
    answer = 0

    repeat = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '?':
                repeat.append((i, j))

    permutations = list(product(['a', 'b', 'c'], repeat=len(repeat)))

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    for index, permutation in enumerate(permutations):
        graph = []

        for x in grid:
            tmp = []
            for cha in x:
                tmp.append(cha)

            graph.append(tmp)

        for i, v in enumerate(repeat):
            graph[v[0]][v[1]] = permutation[i]

        dq = deque()
        checked = []
        cnt = 0
        for i in range(len(graph)):
            for j in range(len(graph[i])):
                if graph[i][j] != 0 and graph[i][j] not in checked:
                    cnt += 1
                    prev = graph[i][j]
                    checked.append(graph[i][j])
                    graph[i][j] = 0
                    dq.append((i, j))

                    while dq:
                        tmp = dq.popleft()

                        for k in range(4):
                            x = tmp[0] + dx[k]
                            y = tmp[1] + dy[k]
                            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and prev == graph[x][y]:
                                cnt += 1
                                graph[x][y] = 0
                                dq.append((x, y))

        if cnt == len(grid) * len(grid[0]):
            answer += 1

    return answer


solution(["??b", "abc", "cc?"])
solution(["abcabcab", "????????"])
solution(["aa?"])
