# 내 문제 풀이
import re

'''
정규패턴식 앞에 r이 붙어 있는 경우가 많다. 
파이썬 정규식에는 Raw string이라고 해서, 컴파일 해야 하는 정규식이
Raw String(순수한 문자)임을 알려줄 수 있도록 문법이 있다.

만약 p = re.compile('\section') 이라고 쓴다면 
\s는 공백문자를 의미하는 [ \t\n\r\f\v]이 되어버려서 
원하는 결과를 찾지 못한다. 
그래서 #10번에서 배웠듯이 이스케이프 \를 활용해 \section이라고 해주면 되지만, 
파이썬은 특수하게 r을 사용하면 
백슬래쉬를 1개만 써도 두개를 쓴 것과 같은 효과를 갖는다.
'''
s = re.sub(r'[^0-9]', '', input())
cnt = 0
for i in range(1, s + 1):
    if s % i == 0:
        cnt += 1

print(s, cnt, sep='\n')

# 강의 문제풀이
s = input()
res = 0
for x in s:
    if x.isdecimal():
        res = res * 10 + int(x)

print(res)

cnt = 0
for i in range(1, res + 1):
    if res % 1 == 0:
        cnt += 1

print(cnt)
