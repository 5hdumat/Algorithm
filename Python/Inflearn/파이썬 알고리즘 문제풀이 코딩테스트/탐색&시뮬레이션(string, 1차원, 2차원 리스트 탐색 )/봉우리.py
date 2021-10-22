'''
5
5 3 7 2 3
3 7 1 6 1
7 2 5 3 4
4 3 6 4 1
8 7 3 5 2
'''
# 내 문제 풀이
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

a.insert(0, [0] * n)
a.append([0] * n)

for x in a:
    x.insert(0, 0)
    x.append(0)

cnt = 0

for i in range(1, n + 1):
    for j in range(1, n + 1):
        spot = a[i][j]

        if a[i - 1][j] < spot and a[i + 1][j] < spot and a[i][j - 1] < spot and a[i][j + 1] < spot:
            cnt += 1

print(cnt)

# 강의 문제 풀이
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

a.insert(0, [0] * n)
a.append([0] * n)

for x in a:
    x.insert(0, 0)
    x.append(0)

cnt = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if all(a[i][j] > a[i + dx[k]][j+dy[k]] for k in range(4)):
            cnt += 1

print(cnt)
