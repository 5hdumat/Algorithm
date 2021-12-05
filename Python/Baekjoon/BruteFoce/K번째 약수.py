# https://www.acmicpc.net/problem/2501
n, k = map(int, input().split())
cnt = 0

for i in range(1, n + 1):
    v = n % i

    if v == 0:
        cnt += 1

    if cnt == k:
        print(i)
        break
else:
    print(0)
