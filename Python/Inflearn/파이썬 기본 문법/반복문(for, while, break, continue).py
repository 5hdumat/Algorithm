'''
반복문 (for, while)
'''

# 반복문 알기 전 ragne 함수를 알아야한다.
# range는 정수 리스트를 만들어 변수에 할당한다.
# 출력할 떈 list 형태로 출력해야 하므로 list 함수로 감싼다.

# 0부터 9까지
a = range(10)
print(list(a))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 1부터 9까지
a = range(1, 10)

for i in range(10):
    print(i) # 0부터 9까지 순차 출력

for i in range(1, 11):
    print(i) # 1부터 10까지 순차 출력

for i in range(10, 0):
    print(i) # 아무일도 일어나지 X

for i in range(10, 0, -1):
    print(i) # 10부터 순차적으로 1씩 뺴서 출력

i = 1
while i <= 10:  # 1부터 10까지 출력
    print(i)
    i += 1

i = 10
while i >= 1:  # 10부터 순차적으로 1씩 뺴서 출력
    print(i)
    i -= 1

i = 1
while True:  # True는 항상 참이기 떄문에 무한반복
    if i > 10: # 10까지 출력
        break
    print(i)
    i += 1

for i in range(1, 11): # 홀수만 출력하기
    if i % 2 == 0:
        continue

    print(i)

'''
(번외)
for else 구문도 있다. 
반복문이 조건대로 온전히 돌았을 때 마지막에 else를 한번 더 호출한다.
(but. 중간에 break 가 있으면 거기까지만 출력됨)
'''
for i in range(1, 11):
    print(i)
    # if i == 5:
    #     break
else:
    print(11)