'''
5
1 2
2 3
3 4
4 5
2 4
5 3
-1 -1
'''

n = int(input())
dy = [[100] * (n + 1) for _ in range(n + 1)]
res = [0] * n
for i in range(n + 1):
    dy[i][i] = 0

while True:
    i, j = map(int, input().split())

    if i < 0 or j < 0:
        break

    dy[i][j] = 1
    dy[j][i] = 1

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dy[i][j] = min(dy[i][j], dy[i][k] + dy[k][j])

for i in range(1, n + 1):
    res[i - 1] = max(dy[i][1:])

num = min(res)
print(num, res.count(num))

for i, v in enumerate(res):
    if v == num:
        print(i + 1, end=' ')

# 강의 문제 풀이

n = int(input())
dy = [[100] * (n + 1) for _ in range(n + 1)]
for i in range(n + 1):
    dy[i][i] = 0

while True:
    i, j = map(int, input().split())

    if i < 0 or j < 0:
        break

    dy[i][j] = 1
    dy[j][i] = 1

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dy[i][j] = min(dy[i][j], dy[i][k] + dy[k][j])

# 출력
res = [0] * (n + 1)
score = 100
for i in range(1, n + 1):
    for j in range(1, n + 1):
        res[i] = max(res[i], dy[i][j])
    score = min(score, res[i])

out = []
for i in range(1, n + 1):
    if res[i] == score:
        out.append(i)

print("%d %d" % (score, len(out)))

for x in out:
    print(x, end=' ')
