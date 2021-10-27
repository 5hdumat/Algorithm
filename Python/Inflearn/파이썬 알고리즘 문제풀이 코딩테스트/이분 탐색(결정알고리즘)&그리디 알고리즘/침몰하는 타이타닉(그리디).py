'''
5 140
90 50 70 100 60
'''
from collections import deque

# 강의 문제 풀이
n, limit = map(int, input().split())
p = list(map(int, input().split()))

p.sort()
p = deque(p) # 데크를 쓰자! 데크를 쓰지 않으면 첫 번쨰 요소를 팝할때 뒤 요소를 앞으로 당기는 연산을 하므로 비효율적
cnt = 0

while p:
    # 승객이 1명일 때 예외처리
    # 이 예외처리를 하지 않으면 하단 else 문 p.pop에서 오류남
    if len(p) == 1:
        cnt += 1
        break

    if p[0] + p[-1] > limit:
        p.pop()
        cnt += 1
    else:
        p.popleft()
        p.pop()
        cnt += 1

print(cnt)
