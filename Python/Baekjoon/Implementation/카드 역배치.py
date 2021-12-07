'''
5 10
9 13
1 2
3 4
5 6
1 2
3 4
5 6
1 20
1 20
'''
# https://www.acmicpc.net/problem/10804

card = [x for x in range(1, 21)]

for _ in range(10):
    s, e = map(int, input().split())

    card[s - 1:e] = card[s-1:e][::-1]

print(*card)
