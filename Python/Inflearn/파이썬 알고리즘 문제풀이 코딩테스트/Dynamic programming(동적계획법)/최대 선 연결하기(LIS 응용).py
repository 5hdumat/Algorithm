'''
10
4 1 2 3 9 7 5 6 10 8

선이 안겹치게 하려면 증가수열만 구하면된다.
'''
n = int(input())
arr = list(map(int, input().split()))
arr.insert(0, 0)
dy = [0] * (n + 1)
dy[1] = 1
res = 0

for i in range(2, n + 1):
    tmp = 0

    for j in range(i - 1, 0, -1):
        if arr[i] > arr[j] and dy[j] > tmp:
            tmp += dy[j]

    dy[i] = tmp + 1

    if dy[i] > res:
        res = dy[i]

print(res)
