import collections


def solution(v):
    graph_x = collections.defaultdict(int)
    graph_y = collections.defaultdict(int)

    for x, y in v:
        graph_x[x] += 1
        graph_y[y] += 1

    x = sorted(graph_x.items(), key=lambda x: x[1])[0][0]
    y = sorted(graph_y.items(), key=lambda x: x[1])[0][0]

    return [x, y]


solution([[1, 4], [3, 4], [3, 10]])
solution([[1, 1], [2, 2], [1, 2]])
