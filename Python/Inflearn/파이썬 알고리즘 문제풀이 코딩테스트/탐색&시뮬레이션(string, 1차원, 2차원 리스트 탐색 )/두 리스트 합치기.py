# # 내 문제풀이(nlogn)
# res = []
#
# for _ in range(2):
#     n = int(input())
#     res += list(map(int, input().split()))
#
# res.sort()
#
# print(*res)

# 내 문제풀이 개선 (투포인터)
a = []
b = []
res = []
p1 = 0
p2 = 0

n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

for i in range(n + m):
    if a[p1] <= a[p2]:
        res.append(a[p1])
        p1 += 1

        if p1 == len(a):
            res += b[p2:]
            break

    else:
        res.append(b[p2])
        p2 += 1

        if p2 == len(b):
            res += a[p1:]
            break

print(*res)

# 강의 문제 풀이
n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

p1 = p2 = 0

c = []

while p1 < n and p2 < m:
    if a[p1] <= b[p2]:
        c.append(a[p1])
        p1 += 1

    else:
        c.append(b[p2])
        p2 += 1

if p1 < n:
    c += a[p1:]

if p2 < m:
    c += b[p2:]

for x in c:
    print(x, end=' ')
