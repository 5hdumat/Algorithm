# https://www.acmicpc.net/problem/1929
m, n = map(int, input().split())

index = 0
prime_check = [True] * (n + 1)

for i in range(m, n + 1):
    for j in range(i*2, n + 1, i):
        print(j)