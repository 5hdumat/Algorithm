import collections
import heapq


def solution(n, edges):
    graph = collections.defaultdict(list)
    heap = []

    for edge in edges:
        graph[edge[1]].append((edge[0], 1))
        # graph[edge[0]].append((edge[1], 1))

    print(graph)
    Q = [[0, min(graph)]]
    dist = collections.defaultdict(list)

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


solution(5, [[0, 1], [0, 2], [1, 3], [1, 4]])
