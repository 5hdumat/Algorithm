'''
0 0 0 0 0 0 0
0 1 1 1 1 1 0
0 0 0 1 0 0 0
1 1 0 1 0 1 1
1 1 0 0 0 0 1
1 1 0 1 1 0 0
1 0 0 0 0 0 0
'''


def dfs(x, y):
    global cnt

    if x == 6 and y == 6:
        cnt += 1
        return
    else:
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]

            if 0 <= tx <= 6 and 0 <= ty <= 6 and a[tx][ty] == 0 and check[tx][ty] == 0:
                check[tx][ty] = 1
                dfs(tx, ty)
                check[tx][ty] = 0


if __name__ == "__main__":
    a = [list(map(int, input().split())) for _ in range(7)]

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    check = [[0] * 7 for _ in range(7)]
    check[0][0] = 1

    cnt = 0
    dfs(0, 0)
    print(cnt)

# 강의 문제 풀이
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def DFS(x, y):
    global cnt

    if x == 6 and y == 6:
        cnt += 1
        return

    else:
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]

            if 0 <= xx <= 6 and 0 <= yy <= 6 and board[xx][yy] == 0:
                board[xx][yy] = 1
                DFS(xx, yy)
                board[xx][yy] = 0

if __name__ == "__main__":
    board = [list(map(int, input().split())) for _ in range(7)]
    cnt = 0
    board[0][0] = 1  # 시작 지점 미리 체크
    DFS(0, 0)
    print(cnt)
