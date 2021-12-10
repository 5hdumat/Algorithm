'''
stack: LIFO
'''
from collections import deque

n, m = map(int, input().split())
n = deque(list(map(int, str(n))))

stack = []
cnt = 0
while len(n) > 0:
    tmp = n.popleft()

    if len(stack) == 0:
        stack.append(tmp)
        continue

    for _ in range(len(stack)):
        if stack[-1] < tmp and m > 0:
            stack.pop()
            m -= 1
        elif stack[-1] > tmp:
            stack.append(tmp)
            break
    else:
        stack.append(tmp)

if m == 0:
    print(*stack, sep='')
else:
    print(*stack[:-m], sep='')  # 슬라이싱을 -2까지 하면 9977252641에서 99772526 출력

# 강의 문제 풀이

num, m = map(int, input().split())
num = list(map(int, str(num)))
stack = []

for x in num:
    # stack이 비어있지 않고 m이 0보다 크고 stack의 가장 마지막 인자가 x보다 작으면 반복문 돌리기
    while stack and m > 0 and stack[-1] < x:
        stack.pop()
        m -= 1
    stack.append(x)

if m != 0:
    stack = stack[:-m]

res = ''.join(map(str, stack))
print(res)

