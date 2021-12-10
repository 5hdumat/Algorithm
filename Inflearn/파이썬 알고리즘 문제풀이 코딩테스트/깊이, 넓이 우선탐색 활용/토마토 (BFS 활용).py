'''
6 4
0 0 -1 0 0 0
0 0 1 0 -1 0
0 0 -1 0 0 0
0 0 0 0 -1 1
'''
# 최단거리 문제는 BFS 활용하자!
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(m)]
dis = [[0] * n for _ in range(m)]

Q = deque()

# 일단 시작지점 싹 정리
for i in range(m):
    for j in range(n):
        if board[i][j] == 1:
            Q.append((i, j))

while Q:
    tmp = Q.popleft()

    for i in range(4):
        x = tmp[0] + dx[i]
        y = tmp[1] + dy[i]

        if 0 <= x < m and 0 <= y < n and board[x][y] == 0:
            dis[x][y] = dis[tmp[0]][tmp[1]] + 1
            board[x][y] = 1
            Q.append((x, y))

flag = True
for i in range(m):
    for j in range(n):
        if board[i][j] == 0:
            flag = False
            break

if flag:
    res = 0
    for i in range(m):
        for j in range(n):
            if dis[i][j] > res:
                res = dis[i][j]

    print(res)
else:
    print(-1)