n, k = map(int, input().split())
measure = []

for i in range(1, n + 1):
    if n % i == 0:
        measure.append(i)

if len(measure) >= k:
    measure.sort()
    print(measure[k - 1])
else:
    print(-1)

# 개선
n, k = map(int, input().split())
cnt = 0

for i in range(1, n + 1):
    if n % i == 0:
        cnt += 1

    if cnt == k:
        print(i)
        break
else:
    print(-1)
