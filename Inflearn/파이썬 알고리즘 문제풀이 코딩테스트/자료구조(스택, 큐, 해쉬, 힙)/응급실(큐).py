'''
queue: FIFO

5 2
60 50 70 80 90

6 0
60 60 90 60 60 60
'''
from collections import deque

n, m = map(int, input().split())
Q = [(i, v) for i, v in enumerate(list(map(int, input().split())))]
Q = deque(Q)
cnt = 0

while True:
    cur = Q.popleft()

    if any(cur[1] < x[1] for x in Q): # any(iterable)은 반복 가능한 자료형을 인자로 받아 단 하나라도 참이 있으면 참 반환
        Q.append(cur)
        continue
    else:
        cnt += 1

    if cur[0] == m:
        break

print(cnt)

# 강의 문제 풀이
from collections import deque

n, m = map(int, input().split())
Q = [(i, v) for i, v in enumerate(list(map(int, input().split())))]
Q = deque(Q)
cnt = 0

while True:
    cur = Q.popleft()

    if any(cur[1] < x[1] for x in Q): # any(iterable)은 반복 가능한 자료형을 인자로 받아 단 하나라도 참이 있으면 참 반환
        Q.append(cur)
    else:
        cnt += 1
        if cur[0] == m:
            break

print(cnt)