# https://www.acmicpc.net/problem/2506
'''
10
1 0 1 1 1 0 0 1 1 0
'''
n = int(input())
arr = list(map(int, input().split()))

status = 0
res = 0
for x in arr:
    if x == 1:
        status += 1
        res += status
    else:
        status = 0

print(res)
