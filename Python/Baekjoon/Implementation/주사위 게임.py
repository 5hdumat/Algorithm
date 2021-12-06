'''
3
3 3 6
2 2 2
6 2 5
'''
# https://www.acmicpc.net/problem/2476

n = int(input())

res = 0
for _ in range(n):
    a, b, c = map(int, input().split())

    if a == b == c:
        tmp = 10000 + (a * 1000)

    elif a == b or b == c or a == c:
        if a == b or a == c:
            tmp = 1000 + (a * 100)
        elif b == c:
            tmp = 1000 + (b * 100)

    elif a != b != c:
        m = max(a, b, c)

        tmp = m * 100

    if res < tmp:
        res = tmp

print(res)
