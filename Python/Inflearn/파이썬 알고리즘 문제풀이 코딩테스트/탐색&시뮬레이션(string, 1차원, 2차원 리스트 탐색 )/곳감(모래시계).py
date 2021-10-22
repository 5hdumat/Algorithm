'''
5
10 13 10 12 15
12 39 30 23 11
11 25 50 53 15
19 27 29 37 27
19 13 30 13 19
3
2 0 3
5 1 2
3 1 4
'''

# 내 문제풀이
n = int(input())
persimmons = [list(map(int, input().split())) for _ in range(n)]
m = int(input())

# 회전
for _ in range(m):
    a, b, c = map(int, input().split())

    for _ in range(c):
        if b == 0:
            persimmons[a - 1].append(persimmons[a - 1].pop(0))
        else:
            persimmons[a - 1].insert(0, persimmons[a - 1].pop())

# 모래시계 모양으로 곶감세기
s = 0
e = n
persimmon = 0
for i in range(n):
    for j in range(s, e):
        persimmon += persimmons[i][j]

    if i < n // 2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1

print(persimmon)

# 강의 문제 풀이
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
m = int(input())

for i in range(m):
    h, t, k = map(int, input().split())

    if t == 0:
        for _ in range(k):
            a[h-1].append(a[h - 1].pop(0))
    else:
        for _ in range(k):
            a[h - 1].insert(0, a[h - 1].pop())

res = 0
s = 0
e = n-1

for i in range(n):
    for j in range(s, e+1):
        res += a[i][j]

    if i < n // 2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1

print(res)


