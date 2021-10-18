# 내 문제풀이
# card = list(range(1, 21))
#
# for _ in range(10):
#     start, end = map(int, input().split())
#
#     card[start-1:end] = card[start-1:end][::-1]
#
# print(*card)

# 강의 문제풀이
a = list(range(21))

for _ in range(10):
    s, e = map(int, input().split())

    for i in range((e - s + 1) // 2):
        a[s+i], a[e-i] = a[e-i], a[s+i]

a.pop(0)
for x in a:
    print(x, end=' ')
