'''
3
1 2 5
15

4
1 2 5 7
14
'''

import sys


def dfs(l, sum):
    global res

    if l > res:
        return

    if sum > m:
        return

    if sum == m:
        if l <= res:
            res = l
    else:
        for i in range(n):
            dfs(l + 1, sum + c[i])


if __name__ == "__main__":
    n = int(sys.stdin.readline())
    c = list(map(int, sys.stdin.readline().split()))
    m = int(sys.stdin.readline())

    res = 9999999999999

    dfs(0, 0)
    print(res)

# 강의 문제 풀이 (큰 동전부터 카운트)
import sys


def dfs(l, sum):
    global res

    if sum > m:
        return

    if  l > res:
        return

    if sum == m:
        print(l)
        sys.exit(0)

    else:
        for i in range(n):
            dfs(l + 1, sum + c[i])


if __name__ == "__main__":
    n = int(sys.stdin.readline())
    c = list(map(int, sys.stdin.readline().split()))
    m = int(sys.stdin.readline())

    res = 9999999999999

    c.sort(reverse=True)
    dfs(0, 0)
    print(res)
