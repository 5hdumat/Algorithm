'''
5
6 8 2 6 2
3 2 3 4 6
6 7 3 3 2
7 2 5 3 6
8 9 5 2 7
'''
# BFS 문제풀이
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

Q = deque()

cnt = 0
res = []

for rain in range(100):
    cnt = 0
    ch = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if board[i][j] > rain and ch[i][j] == 0:
                cnt += 1
                Q.append((i, j))
                ch[i][j] = 1

                while Q:
                    tmp = Q.popleft()

                    for k in range(4):
                        x = tmp[0] + dx[k]
                        y = tmp[1] + dy[k]

                        if 0 <= x < n and 0 <= y < n and ch[x][y] == 0 and board[x][y] > rain:
                            ch[x][y] = 1
                            Q.append((x, y))

    if cnt == 0:
        break

    res.append(cnt)

print(max(res))


# 강의 문제 풀이(DFS)
def DFS(x, y, h):
    ch[x][y] = 1
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]

        if 0 <= xx < n and 0 <= yy < n and ch[xx][yy] == 0 and board[xx][yy] > h:
            DFS(xx, yy, h)


if __name__ == "__main__":
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    n = int(input())
    cnt = 0
    res = 0
    board = [list(map(int, input().split())) for _ in range(n)]

    for h in range(100):
        cnt = 0
        ch = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if board[i][j] > h and ch[i][j] == 0:
                    cnt += 1
                    DFS(i, j, h)

        res = max(res, cnt)

        if cnt == 0:
            break

print(res)