# 내 문제풀이
n = int(input())
result = 0

for _ in range(0, n):
    check = [0] * 6
    dice_number = list(map(int, input().split()))

    for i in dice_number:
        check[i - 1] += 1

    max_num = max(check)
    index = check.index(max_num) + 1

    if max_num == 3:
        tmp = 10000 + (index * 1000)
    elif max_num == 2:
        tmp = 1000 + (index * 100)
    else:
        tmp = max_num * 100

    if tmp > result:
        result = tmp

print(result)

# 강의 문제풀이

n = int(input())
res = 0

for i in range(n):
    tmp = input().split()
    tmp.sort()
    a, b, c = map(int, tmp)

    if a == b and b == c:
        money = 10000 + (a * 1000)
    elif a == b or a == c:
        money = 1000 + (a * 100)
    elif b == c:
        money = 1000 + (b * 100)
    else:
        money = c * 100

    if money > res:
        res = money

print(res)
