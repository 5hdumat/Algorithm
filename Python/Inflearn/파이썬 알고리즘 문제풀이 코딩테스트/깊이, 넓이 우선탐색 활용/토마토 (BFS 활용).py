'''
6 4
0 0 -1 0 0 0
0 0 1 0 -1 0
0 0 -1 0 0 0
0 0 0 0 -1 1
'''
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(m)]
dis = [[0] * n for _ in range(m)]

day = 0
Q = deque()

for i in range(m):
    for j in range(n):
        if board[i][j] == 1:
            dis += 1
            Q.append((i, j))

            while Q:
                tmp = Q.popleft()

                for i in range(4):
                    x = tmp[0] + dx[i]
                    y = tmp[1] + dy[i]

                    if 0 <= x < m and 0 <= y < n and board[x][y] == 0:
                        board[x][y] = 1

print(day)
