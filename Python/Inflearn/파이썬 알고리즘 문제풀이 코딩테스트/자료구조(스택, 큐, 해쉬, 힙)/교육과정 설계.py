'''
CBA
3
CBDAGE
FGCDAB
CTSBDEA
'''
from collections import deque, OrderedDict

essential = input()
plans = [deque(list(input())) for _ in range(int(input()))]

for index, plan in enumerate(plans):
    tmp = []

    while plan:
        cur = plan.popleft()

        if any(cur == x for x in essential):
            tmp.append(cur)

    tmp = ''.join(OrderedDict.fromkeys(tmp))

    if essential == tmp:
        print("#%d YES" % (index + 1))
    else:
        print("#%d NO" % (index + 1))
