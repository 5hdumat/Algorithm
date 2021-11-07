# 파이썬 내장함수 풀이

from itertools import product

n, m = map(int, input().split())
n = [x for x in range(1, n + 1)]

res = list(product(n, repeat=m))

for x in res:
    print(x[0], x[1])

print(len(res))

#  DFS 풀이
import sys

input = sys.stdin.readline

def dfs(l):
    global cnt

    if l == m:
        cnt += 1
        print(*res)
        return
    else:
        for i in range(1, n + 1):
            res[l] = i + 1
            dfs(l + 1)


if __name__ == "__main__":
    n, m = map(int, input().rstrip().split())
    cnt = 0
    res = [0] * m

    dfs(0)
    print(cnt)
