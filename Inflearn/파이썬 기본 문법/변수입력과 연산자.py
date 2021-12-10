'''
값 입력받기
'''
a = input("숫자를 입력하세요: ")
print(a)

'''
값 여러개 입력받기 (split은 입력한 값을 띄어쓰기로 구분하여 변수에 할당한다.)
'''
a, b = input("숫자를 입력하세요: ").split()
print(a, b)
print(a + b)  # a와 b에 더하기 연산자를 사용하면 값이 더해지지 않고 문자가 연결된다.
print(type(a))  # <class 'str'> 기본적으로 입력값은 str 이기 때문이다.

'''
숫자로 입력받기
'''
# map()을 사용하여 입력 받은 값을 int 타입으로 변경할 수 있다.
a, b = map(int, input("숫자를 입력하세요: ").split())

# (2 1 입력)
print(a + b)  # (더하기) 3
print(a - b)  # (빼기) 1
print(a * b)  # (곱하기) 2
print(a / b)  # (나누기) 2.0
print(a // b)  # (몫) 2
print(a % b)  # (나머지)) 0
print(a ** b)  # (제곱) 2

'''
실수와 정수를 사칙연산하면?
당연하게도 실수이다.
'''
a = 4.3
b = 5
c = a+b
print(c) # 9.3
print(type(c)) # <class 'float'> 즉, 실수 > 정수