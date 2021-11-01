'''
CBA
3
CBDAGE
FGCDAB
CTSBDEA
'''
from collections import deque, OrderedDict
#
# essential = input()
# plans = [deque(list(input())) for _ in range(int(input()))]
#
# for index, plan in enumerate(plans):
#     tmp = []
#
#     while plan:
#         cur = plan.popleft()
#
#         if any(cur == x for x in essential):
#             tmp.append(cur)
#
#     tmp = ''.join(OrderedDict.fromkeys(tmp))
#
#     if essential == tmp:
#         print("#%d YES" % (index + 1))
#     else:
#         print("#%d NO" % (index + 1))

# 강의 문제 풀이
need = input()
n = int(input())
for i in range(n):
    plan = input()
    dq = deque(need)

    for x in plan:
        if x in dq:
            if x != dq.popleft():
                print("#%d NO" % (i + 1))
                break
    else:
        # dq가 남아있지 않으면 현수는 커리큘럼을 모두 수행한 것
        if len(dq) == 0:
            print("#%d YES" % (i + 1))
        else:
            print("#%d NO" % (i + 1))