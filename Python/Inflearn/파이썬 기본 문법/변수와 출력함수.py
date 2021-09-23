'''
파이썬 변수는
1) 영문과 숫자, _로 이루어진다.
2) 대소문자를 구분한다
3) 문자나, _로 시작한다.
4) 특수문자를 사용하면 안된다.
5) 예약어를 사용하면 안된다. (if, for 등)
'''

a = 1
A = 2
A1 = 3
_a = 4
# 2b = 5 #Error!
# if = 6 #Error!

print(a, A, A1, _a)  # 1 2 3 4

'''
변수 여러개를 한번에 지정 할 수 있다.
'''

a, b, c = 1, 2, 3

print(a, b, c)  # 1 2 3

'''변수끼리 값 교환이 가능하다'''

a, b = 1, 2
a, b = b, a

print(a, b)  # 2 1

'''
변수 타입을 확인
'''

a = 12345
print(type(a))  # <class 'int'>

a = 'student'
print(type(a))  # <class 'str'>

'''파이썬에서 실수는 8byte까지 표현 가능하다.'''

a = 12.123456789123456789123456789
print(a)  # 12.123456789123457
print(type(a))  # <class 'float'>

'''
출력 방식
'''

print('number')  # number

a, b, c = 1, 2, 3

print(a, b, c)  # 1 2 3
print('number: ', a, b, c)  # number:  1 2 3

# print는 자동으로 띄어쓰기를 하는데 sep을 쓰면 줄바꿈이 없도록 강제할 수 있다.
print(a, b, c, sep='') # 123
print(a, b, c, sep=',') # 1,2,3
print(a, b, c, sep='\n') # 1 2 3 세로로 출력

print(a)
print(b)
print(c) # 1 2 3 세로로 출력

# print는 자동으로 줄바꿈을 하는데 end를 쓰면 줄바꿈이 없도록 강제할 수 있다.
print(a, end=' ')
print(b, end=' ')
print(c, end=' ') # 1 2 3