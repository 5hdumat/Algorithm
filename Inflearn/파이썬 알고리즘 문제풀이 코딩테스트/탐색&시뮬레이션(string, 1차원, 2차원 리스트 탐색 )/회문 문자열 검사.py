# 내 문제풀이
n = int(input())
result = []

for _ in range(n):
    word = input().lower()

    pointer1 = 0
    pointer2 = len(word) - 1
    cnt = len(word) // 2

    for _ in range(cnt):
        if word[pointer1] == word[pointer2]:
            pointer1 += 1
            pointer2 -= 1
        else:
            result.append("NO")
            break
    else:
        result.append("YES")

for index, value in enumerate(result):
    print("#%s %s" % (index + 1, value))

# 강의 문제풀이
n = int(input())

for i in range(n):
    s = input()
    s = s.upper()
    size = len(s)

    for j in range(size // 2):
        if s[j] != s[-1 - j]:
            print("#%d NO" % (i + 1))
            break
    else:
        print("#%d YES" % (i + 1))

# 파이썬스럽게
for i in range(n):
    s = input()
    s = s.upper()

    if s == s[::-1]:  # ::-1 하면 문자열을 리버스 시킨다.
        print("#%d YES" % (i + 1))
    else:
        print("#%d NO" % (i + 1))
