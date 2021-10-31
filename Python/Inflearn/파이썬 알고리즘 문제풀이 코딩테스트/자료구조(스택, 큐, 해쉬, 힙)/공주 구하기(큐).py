'''
queue: FIFO

python이 지원하는 queue 라이브러리 -> deque
'''
from collections import deque

n, k = map(int, input().split())
queue = [i for i in range(1, n + 1)]

tmp = 1
while len(queue) > 1:
    # print(queue)
    if tmp == k:
        queue.pop(0)
        tmp = 0
    else:
        queue.append(queue.pop(0))

    tmp += 1

print(queue[0])

# 강의 문제 풀이
n, k = map(int, input().split())
dq = deque(list(range(1, n + 1)))

while dq:
    for _ in range(k-1):
        cur = dq.popleft()
        dq.append(cur)

    dq.popleft()

    if len(dq) == 1:
        print(dq[0])
        dq.popleft()
