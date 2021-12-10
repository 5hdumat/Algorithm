'''
리스트와 내장함수 (2)
'''

a = [23, 12, 36, 53, 19]

# 리스트도 슬라이싱 가능
print(a[:3])  # 23, 12, 36
print(a[1:4])  # 12, 36, 53
print(len(a))  # 5

# 리스트 반복문 출력 방법
for i in range(len(a)):
    print(a[i], end=' ')  # 23 12 36 53 19
print()

for i in a:
    print(i, end=' ')  # 23 12 36 53 19
print()

# 홀수만 출력
for i in a:
    if i % 2 == 1:
        print(i, end=' ')  # 23 53 19
print()

'''
튜플(tuple)
! 리스트와 다른점은 튜플은 값을 변경할 수 없다.
'''

# tuple 자료구조로 출력
# (0, 23) -> 0번 인덱스에 23이 있다.
# (1, 12)
# (2, 36)
# (3, 53)
# (4, 19)
for i in enumerate(a):
    print(i)

# 소괄호는 tuple 대괄호는 list
b = (1, 2, 3, 4, 5)
print(b[0])  # 1

# # 리스트와 다른점은 튜플은 값을 변경할 수 없다.
# b[0] = 7  # Error!

# 인덱스와 값 바로 출력
for index, value in enumerate(a):
    print(index, value)

'''
all()
all()은 리스트의 요소가 모두 참이면 참 (하나라도 거짓이면 거짓)

a = [23, 12, 36, 53, 19] 가정

'''

# all()은 a리스트의 요소가 모두 60 이상이면 참 (하나라도 거짓이면 거짓)
if all(50 > i for i in a):
    print("참")
else:
    print("거짓")  # 거짓

'''
any()
any()는 리스트에 한가지 요소가 참이되면 참

a = [23, 12, 36, 53, 19] 가정

'''

# any()는 a리스트에 한가지 요소가 참이되면 참 (모두 거짓이여야 거짓)
if any(11 > i for i in a):
    print("참")
else:
    print("거짓")  # 거짓
