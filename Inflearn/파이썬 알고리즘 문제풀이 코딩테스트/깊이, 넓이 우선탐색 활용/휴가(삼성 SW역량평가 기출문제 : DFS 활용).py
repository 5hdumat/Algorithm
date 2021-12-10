'''
7
4 20
2 10
3 15
3 20
2 30
2 20
1 10
'''


def dfs(l, sum, time):
    global res

    if l > n:
        return

    if time > n:
        return

    if l == n:
        if res < sum:
            res = sum
    else:
        # if l + t[l] <= n:
        dfs(l + t[l], sum + p[l], time + t[l])
        dfs(l + 1, sum, time)


n = int(input())
t = []
p = []

for _ in range(n):
    a, b = map(int, input().split())

    t.append(a)
    p.append(b)

res = 0
dfs(0, 0, 0)
print(res)


# 강의 문제 풀이
def dfs(L, sum):
    global res

    if L == n + 1:
        if sum > res:
            res = sum

    else:
        if L + T[L] <= n + 1:
            dfs(L + T[L], sum + P[L])
        dfs(L+1, sum)


if __name__ == "__main__":
    n = int(input())
    T = []
    P = []

    for _ in range(n):
        a, b = map(int, input().split())

        T.append(a)
        P.append(b)

    res = 0
    T.insert(0, 0)
    P.insert(0, 0)

    dfs(1, 0)
    print(res)
