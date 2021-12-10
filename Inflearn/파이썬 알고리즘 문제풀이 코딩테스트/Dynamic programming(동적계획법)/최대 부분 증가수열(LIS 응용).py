'''
8
5 3 7 8 6 2 9 4
'''
n = int(input())
arr = list(map(int, input().split()))
dy = [0] * (n + 1)
res = 0
for i in range(n):
    tmp = 0

    if i == 0:
        dy[1] = 1
        continue

    for j in range(0, i):
        if arr[j] < arr[i] and dy[j] > tmp:
            tmp = dy[j]

    dy[i] = tmp + 1

    if dy[i] > res:
        res = dy[i]

print(res)

# 강의 문제 풀이
n = int(input())
arr = list(map(int, input().split()))
arr.insert(0, 0)
dy = [0] * (n + 1)
dy[1] = 1
res = 0

for i in range(2, n + 1):
    max = 0

    for j in range(i-1, 0, -1):
        if arr[j] < arr[i] and dy[j] > max:
            max = dy[j]

    dy[i] = max + 1

    if dy[i] > res:
        res = dy[i]

print(res)