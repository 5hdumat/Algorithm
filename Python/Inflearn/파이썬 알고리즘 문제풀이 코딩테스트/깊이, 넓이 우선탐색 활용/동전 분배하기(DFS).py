'''
7
8
9
11
12
23
15
17
'''


def dfs(l):
    global res

    if l == N:
        tmp = set()
        for x in money:
            tmp.add(x)

        if len(tmp) == 3:
            dif = max(money) - min(money)

            if res > dif:
                res = dif

    else:
        for i in range(len(money)):
            money[i] += c[l]
            dfs(l + 1)
            money[i] -= c[l]

N = int(input())
c = [int(input()) for _ in range(N)]

money = [0, 0, 0]
ch = [0] * (N + 1)
res = 9999999999
dfs(0)
print(res)
