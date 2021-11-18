'''
0 0 0 0 0 0 0
0 1 1 1 1 1 0
0 0 0 1 0 0 0
1 1 0 1 0 1 1
1 1 0 1 0 0 0
1 0 0 0 1 0 0
1 0 1 0 0 0 0
'''
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

a = [list(map(int, input().split())) for _ in range(7)]

dq = deque()
dq.append((0, 0))

while dq:
    tmp = dq.popleft()

    for i in range(4):
        x = tmp[0] + dx[i]
        y = tmp[1] + dy[i]

        if 0 <= x <= 6 and 0 <= y <= 6 and a[x][y] == 0:
            a[x][y] = 1
            a[x][y] = a[tmp[0]][tmp[1]] + 1
            dq.append((x, y))

# for x in dis:
#     print(x)

print(a[6][6])