'''
4 11
802
743
457
539
'''
# 내 문제풀이
n, m = map(int, input().split())
a = []

for _ in range(n):
    a.append(int(input()))

lt = 0
rt = max(a)

while lt <= rt:
    mid = (lt + rt) // 2

    # 강의에선 이 이부분을 함수로 뺌
    cnt = 0

    for i in a:
        cnt += i // mid
    # 강의에선 이 이부분을 함수로 뺌

    if cnt < m:
        rt = mid
    elif cnt > m:
        lt = mid
    else:
        print(mid)
        break


# 강의 문제 풀이
def Count(len):
    cnt = 0

    for x in line:
        cnt += x // len

    return cnt


k, n = map(int, input().split())
line = []
largest = 0

for _ in range(k):
    tmp = int(input())
    line.append(tmp)
    largest = max(largest, tmp)  # 두 인자를 비교해 더 큰 값을 할당

lt = 1
rt = largest
res = 0
while lt <= rt:
    mid = (lt + rt) // 2

    if Count(mid) >= n:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(res)
