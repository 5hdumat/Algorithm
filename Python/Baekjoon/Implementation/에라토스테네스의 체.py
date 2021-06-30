# https://www.acmicpc.net/problem/2960
n, k = map(int, input().split())

index = 0
prime_check = [True] * (n + 1)

for i in range(2, n + 1):
    for j in range(i, n + 1, i):
        if prime_check[j]:
            prime_check[j] = False
            index += 1
            
            if index == k:
                print(j)
    