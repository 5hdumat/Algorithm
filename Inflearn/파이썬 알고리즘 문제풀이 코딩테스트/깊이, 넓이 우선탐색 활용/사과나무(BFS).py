'''
5
10 13 10 12 15
12 39 30 23 11
11 25 50 53 15
19 27 29 37 27
19 13 30 13 19
'''
from collections import deque

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

dq = deque()
ch = [[0] * n for _ in range(n)]

dq.append((n // 2, n // 2))
ch[2][2] = 1

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

cnt = a[n // 2][n // 2]
L = 0
while True:
    if L == n // 2:
        print(cnt)
        break

    for i in range(len(dq)):
        tmp = dq.popleft()

        for j in range(4): # 상하좌우 탐색
            x = tmp[0] + dx[j]
            y = tmp[1] + dy[j]

            if ch[x][y] == 0:
                cnt += a[x][y]

                ch[x][y] = 1
                dq.append((x, y))


    # print("레벨: ", L)
    # for x in ch:
    #     print(x)

    L += 1

