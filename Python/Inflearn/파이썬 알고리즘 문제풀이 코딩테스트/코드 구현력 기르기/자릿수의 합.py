# 내 문제풀이
n = int(input())
number_list = list(map(int, input().split()))
max = 0


def digit_sum(x):
    sum = 0
    for i in str(x):
        sum += int(i)

    return sum


for index, value in enumerate(number_list):
    result = digit_sum(number_list[index])
    if max < result:
        max = result
        index = index

print(number_list[index])

# 강의 문제 풀이
n = int(input())
number_list = list(map(int, input().split()))
max = 0


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


for x in a:
    total = digit_sum(x)

    if total > max:
        max = total
        res = x

print(x)
