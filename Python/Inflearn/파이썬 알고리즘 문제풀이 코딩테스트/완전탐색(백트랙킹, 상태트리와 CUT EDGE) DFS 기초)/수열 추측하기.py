import sys

# def dfs(l):
#     if l == n:
#         sum = 0
#
#         for i, v in enumerate(p):
#             sum += b[i] * v
#
#         if sum == f:
#             print(*p)
#             sys.exit(0)
#     else:
#         for i in range(1, n + 1):
#             if ch[i] == 0:
#                 ch[i] = 1
#                 p[l] = i
#                 dfs(l + 1)
#                 ch[i] = 0
#
#
# n, f = map(int, input().split())
# p = [0] * n
# b = [1] * n
# ch = [0] * (n + 1)
#
# for i in range(1, n):
#     b[i] = (b[i - 1] * (n - i)) / i
#
# b = list(map(int, b))
#
# dfs(0)

# 강의 문제 풀이
import sys

def dfs(l, sum):
    if l == n and sum == f:
        print(*p)
        sys.exit(0)
    else:
        for i in range(1, n + 1):
            if ch[i] == 0:
                ch[i] = 1
                p[l] = i
                dfs(l + 1, sum + (i * b[l]))
                ch[i] = 0

n, f = map(int, input().split())
p = [0] * n
b = [1] * n
ch = [0] * (n + 1)

for i in range(1, n - 1):
    b[i] = b[i - 1] * (n - i) // i

dfs(0, 0)
