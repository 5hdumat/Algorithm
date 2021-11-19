'''
5
2 23 92 78 93
59 50 48 90 80
30 53 70 75 96
94 91 82 89 93
97 98 95 96 100
'''


def DFS(x, y):
    global cnt

    if x == ex and y == ey:
        cnt += 1
        return
    else:
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]

            if 0 <= tx < n and 0 <= ty < n and board[x][y] < board[tx][ty]:
                DFS(tx, ty)


if __name__ == "__main__":
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    sx, sy = 0, 0
    ex, ey = 0, 0

    minn = min(map(min, board))
    maxx = max(map(max, board))
    for i, iv in enumerate(board):
        for j, jv in enumerate(iv):
            if jv == minn:
                sx, sy = i, j

            elif jv == maxx:
                ex, ey = i, j

    cnt = 0
    DFS(sx, sy)
    print(cnt)


# 강의 문제 풀이
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def DFS(x, y):
    global cnt

    if x == ex and y == ey:
        cnt += 1

    else:
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < n and 0 <= yy < n and ch[xx][yy] == 0 and board[xx][yy] > board[x][y]:
                ch[xx][yy] = 1
                DFS(xx, yy)
                ch[xx][yy] = 0


if __name__ == "__main__":
    n = int(input())
    board = [[0] * n for _ in range(n)]
    ch = [[0] * n for _ in range(n)]

    maxx = -2147000000
    minn = 2147000000

    for i in range(n):
        tmp = list(map(int, input().split()))
        for j in range(n):
            if tmp[j] < minn:
                minn = tmp[j]
                sx = i
                sy = j

            if tmp[j] > maxx:
                maxx = tmp[j]
                ex = i
                ey = j

            board[i][j] = tmp[j]

    ch[sx][sy] = 1
    cnt = 0
    DFS(sx, sy)
    print(cnt)


# 내 문제풀이 개선

def DFS(x, y):
    global cnt

    if x == ex and y == ey:
        cnt += 1
        return
    else:
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]

            if 0 <= tx < n and 0 <= ty < n and ch[tx][ty] == 0 and board[x][y] < board[tx][ty]:
                ch[tx][ty] = 1
                DFS(tx, ty)
                ch[tx][ty] = 0


if __name__ == "__main__":
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    ch = [[0] * n for _ in range(n)]

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    sx, sy = 0, 0
    ex, ey = 0, 0

    minn = min(map(min, board))
    maxx = max(map(max, board))
    for i, iv in enumerate(board):
        for j, jv in enumerate(iv):
            if jv == minn:
                sx, sy = i, j

            elif jv == maxx:
                ex, ey = i, j

    ch[sx][sy] = 1
    cnt = 0
    DFS(sx, sy)
    print(cnt)
