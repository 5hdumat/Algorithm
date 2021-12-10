'''
6 6
1 4
5 4
4 3
2 5
2 3
6 2

그래프 정렬은 Queue 활용
'''
from collections import deque

n, m = map(int, input().split())
dir = [[] for _ in range(n + 1)]
degree = [0] * (n + 1)

# 진입차수 구하기
for _ in range(m):
    a, b = map(int, input().split())

    degree[b] += 1
    dir[a].append(b)

Q = deque()

for i in range(1, n + 1):
    if degree[i] == 0:
        Q.append(i)

while Q:
    tmp = Q.popleft()

    print(tmp, end=' ')

    for x in dir[tmp]:
        degree[x] -= 1

        if degree[x] == 0:
            Q.append(x)

# 강의 문제 풀이
n, m = map(int, input().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]
degree = [0] * (n + 1)
dq = deque()

for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    degree[b] += 1

for i in range(1, n + 1):
    if degree[i] == 0:
        dq.append(i)

while dq:
    x = dq.popleft()

    print(x, end=' ')

    for i in range(1, n+1):
        if graph[x][i] == 1:
            degree[i] -= 1

            if degree[i] == 0:
                dq.append(i)
