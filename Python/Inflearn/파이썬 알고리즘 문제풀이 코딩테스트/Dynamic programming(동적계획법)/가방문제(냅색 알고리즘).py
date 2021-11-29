'''
4 11
5 12
3 8
6 14
4 8
'''
n, limit = map(int, input().split())
dy = [0] * (limit + 1)
jewel = []

for _ in range(n):
    a, b = map(int, input().split())

    jewel.append((a, b))

for i in range(n):
    w, v = jewel[i]

    for j in range(w, limit + 1):
        tmp = dy[j - w] + v

        if dy[j] < tmp:
            dy[j] = tmp

print(dy[limit])

# 강의 문제 풀이
n, m = map(int, input().split())
dy = [0] * (m + 1)

for i in range(n):
    w, v = map(int, input().split())

    for j in range(w, m + 1):
        dy[j] = max(dy[j], dy[j - w] + v)

print(dy[m])