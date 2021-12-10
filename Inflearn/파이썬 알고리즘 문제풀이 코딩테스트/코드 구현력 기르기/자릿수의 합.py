n = int(input())
number_list = list(map(int, input().split()))
max = 0


# 사칙연산을 이용해 푸는 방식
# def digit_sum(x):
#     sum = 0
#     while x > 0:
#         sum += x % 10
#         x = x // 10
#
#     return sum

# 파이썬 답게 푸는 방식
def digit_sum(x):
    sum = 0
    for i in str(x):
        sum += int(i)

    return sum


for x in number_list:
    total = digit_sum(x)

    if total > max:
        max = total
        res = x

print(res)


# 복습
def digit_sum(x):
    sum = 0

    while x > 0:
        sum += x % 10
        x = x // 10

    return sum


n = int(input())
arr = list(map(int, input().split()))
max = 0
for x in arr:
    tmp = digit_sum(x)

    if max < tmp:
        max = tmp
        res = x

print(res)
