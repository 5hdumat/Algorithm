# # 강의 문제 풀이
# def reverse(x):
#     res = 0
#     while x > 0:
#         t = x % 10
#         res = res * 10 + t
#         x = x // 10
#
#     return res
#
#
# def isPrime(x):
#     if x == 1:
#         return False
#
#     '''
#     약수는 본인을 제외한 나머지 숫자는 절반부터 시작
#     12 를 예로들면
#     1 * 12 = 12 (본인제외)
#     2 * 6 = 12 <== 절반부터 시작
#     3 * 4 = 12
#
#     그러므로 2로 나눈 몫까지만 반복문을 돌리면 된다.
#     '''
#     for i in range(2, x // 2 + 1):
#         if x % i == 0:
#             return False
#     else:
#         return True
#
#
# n = int(input())
# a = list(map(int, input().split()))
#
# for x in a:
#     tmp = reverse(x)
#     if isPrime(tmp):
#         print(tmp, end=' ')


# 복습

def reverse(x):
    res = 0

    while x > 0:
        t = x % 10

        # print(res, x, t)
        res = res * 10 + t
        x = x // 10

    return res

def isPrime(x):
    for i in range(2, x // 2 + 1):
        if x % i == 0:
            return False
    else:
        return True


n = int(input())
arr = list(map(int, input().split()))

for x in arr:
    tmp = reverse(x)

    if isPrime(tmp):
        print(tmp, end=' ')
