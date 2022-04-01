import collections
import heapq


def solution(n, start, end, roads, traps):
    graph = [[False for _ in range(n + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        graph[i][i] = 0

    # 출발지, 목적지, 비용
    for u, v, w in roads:
        if not graph[u][v]:
            graph[u][v] = w
        else:
            graph[u][v] = min(graph[u][v], w)

    Q = [(0, start, 0)]
    visited = [["미방문" for _ in range(1 << len(traps))] for _ in range(n + 1)]

    while Q:
        cost, node, state = heapq.heappop(Q)

        if node == end:
            print(cost)
            return cost

        # 방문체크
        if visited[node][state] == "방문했었지롱":
            continue

        visited[node][state] = "방문했었지롱"

        trapped = collections.defaultdict(bool)  # 인접한 함정 노드 발동 여부 기록

        for idx, trap in enumerate(traps):
            '''
            트랩이 3개라면
            
            001
            010
            100
            
            와 같은 식으로 하나씩 시프트한 후 & 연사자로 확인할 수 있도록 bit 변수 초기화
            '''
            bit = 1 << idx

            if state & bit:  # 현재 방문한 노드의 트랩이 켜져있다면?
                if node == trap:  # 켜져 있는 노드에 재방문한 경우
                    state &= ~bit  # 현재 비트를 not 연산 후 &연산 (01 & ~01 -> 01 & 10 -> 00

                else:  # 현재 방문 노드가 아니라 인접한 다른 합정 노드는 상태 변경하지 않고, 그대로 기록
                    trapped[trap] = True  # 트랩 발동

            else:  # 현재 방문한 노드가 함정 노드인지 일반 노드인지 모르는 상황에서
                if trap == node:  # 함정 노드라는게 확인이 된다면
                    state |= bit  # 함정 활성화
                    trapped[trap] = True

        for v in range(1, n + 1):
            if node == v:
                continue

            if trapped[node] == trapped[v]:
                if graph[node][v]:
                    heapq.heappush(Q, (cost + graph[node][v], v, state))

            else:
                if graph[v][node]:
                    heapq.heappush(Q, (cost + graph[v][node], v, state))

    return 0

# solution(3, 1, 3, [[1, 2, 2], [3, 2, 3]], [2])
solution(4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3])
# solution(4, 1, 4, [[1, 2, 1], [3, 2, 1], [4, 3, 1]], [2, 3])
# solution(4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1], [4, 3, 1]], [2, 3])
