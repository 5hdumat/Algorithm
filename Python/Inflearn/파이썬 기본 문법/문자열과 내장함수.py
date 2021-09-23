'''
문자열과 내장함수
'''

msg = "It is Time"

# 문자를 모두 대/소문자로 치환
print(msg.upper())  # IT IS TIME
print(msg.lower())  # it is time

# (대문자화 시킨 결과만 출력 기존의 msg 변수는 그대로 있다.)
print(msg)  # It is Time

# 대문자화된 msg를 tmp에 할당
tmp = msg.upper()
print(tmp)  # IT IS TIME

# tmp의 처음으로 발견된 T를 찾아 인덱스 값 리턴
print(tmp.find('T'))

# 문자열에 T가 몇개 있는지 카운트해서 리턴
print(tmp.count('T'))

'''
슬라이싱
msg = "It is Time"
'''

# 왼쪽부터 2글자 출력
print(msg[:2])  # IT

# 3 인덱스부터 4인덱스까지 출력 (5 아님)
print(msg[3:5])

# 문자열 거꾸로 출력
print(msg[::-1])  # emiT si tI

# 5번 인덱스부터 1번 인덱스(0번 까지가 아님)까지 역순 출력
print(msg[5:0:-1])  # si t

# 5번쨰 인덱스부터 출력하는데 맨 끝 1글자 지우기 (-2면 2글자)
print(msg[5:-1])  # Tim

# 문자열 뿐 아니라 리스트나 튜플에도 적용 가능하다.
l = ['a', 'b', 'c', 'd', 'e']
print(l[::-1])  # ['e', 'd', 'c', 'b', 'a']

# 문자열 길이
print(len(msg))  # 10

# 배열로 문자열 인덱스 접근
for i in range(len(msg)):
    print(msg[i], end='')  # It is Time
print()

# 이렇게도 접근 가능하다.
for i in msg:
    print(i, end='')  # It is Time
print()

# 대/소문자만 뽑기
for i in msg:
    # 대문자인지 판단
    if i.isupper():
        print(i, end=' ')  # I T
print()

for i in msg:
    if i.islower():
        print(i, end=' ')  # t i s i m e
print()

# 알파벳만 출력
for i in msg:
    if i.isalpha():
        print(i, end='')  # ItisTime
print()

'''
아스키코드 가져오기
'''

tmp = 'AZ'
for i in tmp:
    print(ord(i), end=' ')  # 65 90
print()

tmp = 'az'
for i in tmp:
    print(ord(i), end=' ')  # 97 122
print()

'''
아스키코드 문자열로 변환하기
'''

tmp = 66
print(chr(tmp))  # B
