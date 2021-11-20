'''
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
'''
import sys


def dfs(x, y):
    global cnt

    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]

        if 0 <= tx < n and 0 <= ty < n and board[tx][ty] == 1:
            cnt += 1
            board[tx][ty] = 0
            dfs(tx, ty)


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n = int(input())
board = [list(map(int, input())) for _ in range(n)]
res = []
cnt = 0

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            cnt = 1
            board[i][j] = 0
            dfs(i, j)
            res.append(cnt)

print(len(res))

res.sort()

for x in res:
    print(x)

# 강의 문제 풀이


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def DFS(x, y):
    global cnt

    cnt += 1
    board[x][y] = 0

    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]

        if 0 <= xx <n and 0 <= yy < n and board[xx][yy] == 1:
            DFS(xx, yy)


if __name__ == "__main__":
    n = int(input())
    board = [list(map(int, input())) for _ in range(n)]
    res = []

    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                cnt = 0
                DFS(i, j)
                res.append(cnt)

res.sort()

print(len(res))
for x in res:
    print(x)