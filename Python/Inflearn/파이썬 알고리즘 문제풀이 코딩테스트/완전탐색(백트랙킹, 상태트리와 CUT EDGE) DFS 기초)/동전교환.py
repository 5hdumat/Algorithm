'''
3
1 2 5
15
'''

import sys


def dfs(l, sum):
    global res

    if sum > m:
        print(res)
        return
    else:
        for i in range(n):
            dfs(l + 1, sum + c[i])


if __name__ == "__main__":
    n = int(sys.stdin.readline())
    c = list(map(int, sys.stdin.readline().split()))
    m = int(sys.stdin.readline())

    res = 0
    dfs(0, 0)
