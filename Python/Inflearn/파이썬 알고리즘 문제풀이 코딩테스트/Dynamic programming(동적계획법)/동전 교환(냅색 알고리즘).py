'''
3
1 2 5
15
'''
n = int(input())
coins = list(map(int, input().split()))
change = int(input())
dy = [change] * (change + 1)

dy[0] = 0
for x in coins:
    dy[x] = 1

for i in range(n):
    coin = coins[i]

    for j in range(coin, change + 1):
        dy[j] = min(dy[j], dy[j - coin] + 1)

print(dy[change])

# 강의 문제 풀이

n = int(input())
coin = list(map(int, input().split()))
m = int(input())
dy = [1000] * (m + 1)

dy[0] = 0
for i in range(n):
    for j in range(coin[i], m + 1):
        dy[j] = min(dy[j], dy[j - coin[i]] + 1)

print(dy[m])