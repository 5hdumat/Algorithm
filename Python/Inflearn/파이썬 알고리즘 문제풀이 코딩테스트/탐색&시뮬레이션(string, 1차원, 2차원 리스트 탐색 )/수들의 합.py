# 내 문제풀이 (n^2)
n, m = map(int, input().split())
a = list(map(int, input().split()))
p1 = 0
p2 = 1
cnt = 0

while p1 <= len(a) and p2 <= len(a):
    total = sum(a[p1:p2])

    if total < m:
        p2 += 1
    elif total == m:
        cnt += 1
        p1 += 1
    elif total > m:
        p1 += 1

print(cnt)

# 강의 문제 풀이 (n)

n, m = map(int, input().split())
a = list(map(int, input().split()))

lt = 0
rt = 1
tot = a[0]
cnt = 0

while True:
    if tot < m:
        if rt < n:
            # print(tot, "+", a[rt])
            tot += a[rt]
            rt += 1
        else:
            break

    elif tot == m:
        # print(tot, "-", a[lt])
        cnt += 1
        tot -= a[lt]
        lt += 1

    else:
        # print(tot, "-", a[lt])
        tot -= a[lt]
        lt += 1

print(cnt)

# 복습 (투포인터)
n, m = map(int, input().split())
arr = list(map(int, input().split()))

lt = 0
rt = 1

sum = arr[0]
cnt = 0

while True:
    if sum < m:
        if rt < n:
            sum += arr[rt]
            rt += 1
        else:
            break

    elif sum == m:
        sum -= arr[lt]
        cnt += 1
        lt += 1

    else:
        sum -= arr[lt]
        lt += 1

print(cnt)
