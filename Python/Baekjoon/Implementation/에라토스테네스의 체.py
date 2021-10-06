# https://www.acmicpc.net/problem/2960

n, k = map(int, input().split())

prime_check = [True] * (n+1)
index = 0
tmp = []

for i in range(2, n+1):
    if prime_check[i]:
        for j in range(i, n+1, i):
            if prime_check[j]:
                prime_check[j] = False
                tmp.append(j)

print(tmp[k-1])