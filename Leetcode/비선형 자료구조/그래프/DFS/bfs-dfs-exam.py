from collections import deque

graph = {
    1: [2, 3],
    2: [5, 4],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3]
}


def dfs(v, discovered=[]):
    discovered.append(v)
    for w in graph[v]:
        if w not in discovered:
            discovered = dfs(w, discovered)

    return discovered

print(dfs(1))

def dfs_stack(start_v):
    discoverd = []
    stack = [start_v]

    while stack:
        p = stack.pop()

        if p not in discoverd:
            discoverd.append(p)

            for x in graph[p]:
                stack.append(x)

    return discoverd

print(dfs_stack(1))

def bfs(start_v):
    discoverd = [start_v]

    q = deque()
    q.append(start_v)

    while q:
        p = q.popleft()

        for x in graph[p]:
            if x not in discoverd:
                discoverd.append(x)
                q.append(x)

    return discoverd

print(bfs(1))
