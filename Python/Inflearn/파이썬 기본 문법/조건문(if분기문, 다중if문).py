'''
분기 if
'''
x = 7
if x == 7:
    print("lucky")

if x != 6:
    print("lucky")

if x > 0:
    print("양수")
else:
    print("음수")

'''
if 다중 조건
'''

# 아래 예제는 하나의 문장 구조이기 때문에 위에서부터 차례대로 비교한다.
# 그러므로 조건이 부합하는 순간 출력된다. (그 다음 조건이 참이라도 무시)
x = 70
if x >= 90:
    print('A')
elif x >= 80:
    print('B')
elif x >= 70:
    print('C')
elif x >= 60:
    print('D')
else:
    print('F')

'''
중첩 if
'''
x = 15
if x >= 10:
    if x % 2 == 1:
        print("x는 10 이상의 홀수이다.")

'''
if 조건에 논리연산자 and
'''
x = 9
if x > 0 and x < 10:
    print("0보다 크고 10보다 작은 자연수")

'''
if 조건에 논리연산자 or
'''
x = -1
if x == 0 or x == -1:
    print("0이거나 -1 이거나")