'''
5 20
10 5
25 12
15 8
6 3
7 4
'''
def dfs(l, sum, time):
    global res

    if time > m:
        return

    if l == n:
        if sum > res:
            res = sum

    else:
        # 문제를 푸는 케이스
        dfs(l + 1, sum + g[l][0], time + g[l][1])

        # 문제를 풀지 않는 케이스
        dfs(l + 1, sum, time)


n, m = map(int, input().split())
g = []
for _ in range(n):
    a, b = map(int, input().split())
    g.append((a, b))

res = 0
dfs(0, 0, 0)
print(res)

