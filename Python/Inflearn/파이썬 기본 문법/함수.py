'''
함수
'''


# 함수 선언
# def = define
def add(a, b):
    c = a + b
    print(c)


# 호출은 무조건 함수 선언 이후에 해야 한다.
add(3, 2)  # 5
add(5, 7)  # 12


def add(a, b):
    c = a + b
    return c


result = add(3, 2)
print(result)  # 5


# 파이썬 함수는 여러개의 값을 리턴 할 수 있다.
# 튜플 구조로 반환
def add(a, b):
    c = a + b
    d = a - b
    return c, d


print(add(3, 2))  # (5, 1)

'''
소수만 출력하는 함수 만들기
! 소수는 1과 자기자신 빼놓고 존재하지 않는 숫자
'''

def isPrime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
        else:
            return True


a = [12, 13, 7, 9, 19]

for i in a:
    # 소수만 출력
    if isPrime(i):
        print(i, end=' ')  # 13 7 9 19
