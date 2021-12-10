'''
1 0 1 0 0 1 0 1 0 1
1 0 1 1 1 1 0 1 0 1
1 0 1 0 0 1 0 1 0 1
1 0 1 0 0 1 0 1 1 1
1 0 1 0 0 1 0 1 0 1
1 0 1 1 1 1 0 1 0 1
1 0 1 0 0 1 0 1 1 1
1 1 1 0 0 1 0 1 0 1
1 0 1 0 0 1 1 1 0 1
1 0 1 0 0 2 0 1 0 1
'''
# import sys
#
# dx = [0, 0]
# dy = [1, -1]
#
#
# def DFS(x, y, s):
#     if board[x][y] == 2:
#         print(s)
#         sys.exit(0)
#
#     ch[x][y] = 1
#
#     for i in range(2):
#         tx = x + dx[i]
#         ty = y + dy[i]
#
#         if 0 <= tx < n and 0 <= ty < n and ch[tx][ty] == 0 and board[tx][ty] == 1:
#             DFS(tx, ty, s)
#             return
#
#     tx = x + 1
#     ty = y
#
#     if 0 <= tx < n and 0 <= ty < n and ch[tx][ty] == 0 and (board[tx][ty] == 1 or board[tx][ty] == 2):
#         DFS(tx, ty, s)
#
#
# if __name__ == "__main__":
#     n = 10
#     board = [list(map(int, input().split())) for _ in range(n)]
#
#     flag = False
#     for i in range(0, n):
#         ch = [[0] * n for _ in range(n)]
#
#         if board[0][i] == 1:
#             DFS(0, i, i)


# 강의 문제 풀이 (강의에선 도착지점에서 출발)
def DFS(x, y):
    ch[x][y] = 1

    if x == 0:
        print(y)
    else:
        if y - 1 > 0 and board[x][y - 1] == 1 and ch[x][y - 1] == 0:  # 좌 사다리 탐색
            DFS(x, y - 1)
        elif y + 1 < 10 and board[x][y + 1] == 1 and ch[x][y + 1] == 0:  # 우 사다리 탐색
            DFS(x, y + 1)
        else:  # 상단 사다리 탐색
            DFS(x - 1, y)


if __name__ == "__main__":
    board = [list(map(int, input().split())) for _ in range(10)]
    ch = [[0] * 10 for _ in range(10)]

    for y in range(10):
        if board[9][y] == 2:
            DFS(9, y)
