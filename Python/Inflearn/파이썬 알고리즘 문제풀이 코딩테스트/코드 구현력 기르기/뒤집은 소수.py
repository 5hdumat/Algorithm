# # 내 문제풀이 1
# def reverse(x):
#     for index, value in enumerate(x):
#         numbers[index] = str(value)[::-1].lstrip('0')
#
#
# def isPrime(x):
#     check_prime = [0] * (x + 1)
#     prime = []
#     for i in range(2, x + 1):
#         if check_prime[i] == 0:
#             prime.append(i)
#             for j in range(i, x + 1, i):
#                 check_prime[j] = 1
#
#     if prime.count(x) > 0:
#         return True
#     else:
#         return False
#
# n = int(input())
# numbers = list(map(int, input().split()))
# result = []
#
# reverse(numbers)
#
# numbers = list(map(int, numbers))
#
# for i in numbers:
#     if isPrime(i):
#         print(i, end=' ')

# # 내 문제풀이 2
# def reverse(x):
#     res = 0  # 1 10
#
#     while x > 0:
#         t = x % 10
#         res = res * 10 + t
#         x = x // 10
#
#     return res
#
#
# def isPrime(x):
#     check_prime = [0] * (x + 1)
#     prime = []
#     for i in range(2, x + 1):
#         if check_prime[i] == 0:
#             prime.append(i)
#             for j in range(i, x + 1, i):
#                 check_prime[j] = 1
#
#     if prime.count(x) > 0:
#         return True
#     else:
#         return False
#
#
# n = int(input())
# numbers = list(map(int, input().split()))
#
# for i in numbers:
#     tmp = reverse(i)
#     if isPrime(tmp):
#         print(tmp, end=' ')


# 강의 문제 풀이
def reverse(x):
    res = 0
    while x > 0:
        t = x % 10
        res = res * 10 + t
        x = x // 10

    return res

def isPrime(x):
    if x == 1:
        return False

    '''
    약수는 본인을 제외한 나머지 숫자는 절반부터 시작
    12 를 예로들면
    1 * 12 = 12 (본인제외)
    2 * 6 = 12 <== 절반부터 시작
    3 * 4 = 12
    
    그러므로 2로 나눈 몫까지만 반복문을 돌리면 된다.
    '''
    for i in range(2, x//2+1):
        if x % i == 0:
            return False
    else:
        return True

n = int(input())
a = list(map(int, input().split()))

for x in a:
    tmp = reverse(x)
    if isPrime(tmp):
        print(tmp, end=' ')

