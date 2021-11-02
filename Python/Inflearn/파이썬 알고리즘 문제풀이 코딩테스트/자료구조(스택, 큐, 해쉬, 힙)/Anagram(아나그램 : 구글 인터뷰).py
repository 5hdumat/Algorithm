'''
AbaAeCe
baeeACA
'''
word1 = input()
word2 = input()

sum = 0
for x in word1:
    sum += hash(x)

for x in word2:
    sum -= hash(x)

if sum == 0:
    print("YES")
else:
    print("NO")

# 강의 문제 풀이1
a = input()
b = input()

sh = dict()

for x in a:
    sh[x] = sh.get(x, 0) + 1

for x in b:
    sh[x] = sh.get(x, 0) - 1

for x in a:
    if sh[x] > 0:
        print("NO")
        break
else:
    print("YES")

# 강의 문제 풀이 2

a = input()
b = input()

str1 = [0] * 52 # 알파벳 대소문자 52개
str2 = [0] * 52

for x in a:
    if x.isupper():
        str1[ord(x) - 65] += 1 # A 아스키코드는 65 이므로 65를 뺴서 인덱스 0부터 시작하도록 함
    else:
        str1[ord(x) - 71] += 1 # a 아스키코드는 98 이므로 71을 빼서 인덱스 26부터 시작하도록 함

for x in b:
    if x.isupper():
        str2[ord(x) - 65] += 1 # A 아스키코드는 65 이므로 65를 뺴서 인덱스 0부터 시작하도록 함
    else:
        str2[ord(x) - 71] += 1 # a 아스키코드는 98 이므로 71을 빼서 인덱스 26부터 시작하도록 함

for i in range(52):
    if str1[i] != str2[i]:
        print("NO")
        break
else:
    print("YES")