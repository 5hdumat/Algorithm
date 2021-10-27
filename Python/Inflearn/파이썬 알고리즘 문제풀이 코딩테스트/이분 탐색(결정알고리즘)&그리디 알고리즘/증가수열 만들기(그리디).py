'''
5
2 4 5 1 3

10
3 2 10 1 5 4 7 8 9 6
'''
n = int(input())
num = list(map(int, input().split()))

cnt = 0
word = ''
last = 0

lt = 0
rt = n - 1
while lt <= rt:
    tmp = []

    if last < num[lt]:
        tmp.append((num[lt], 'L'))

    if last < num[rt]:
        tmp.append((num[rt], 'R'))

    tmp.sort()

    if tmp:
        cnt += 1
        word += tmp[0][1]
        last = tmp[0][0]

        if tmp[0][1] == 'L':
            lt += 1

        else:
            rt -= 1

    else:
        break

print(cnt, word, sep='\n')

# 강의 문제 풀이
n = int(input())
a = list(map(int, input().split()))

lt = 0
rt = n - 1
last = 0

res = ''
tmp = []

while lt <= rt:
    if a[lt] > last:
        tmp.append((a[lt], 'L'))

    if a[rt] > last:
        tmp.append((a[rt], 'R'))

    tmp.sort()

    if len(tmp) == 0:
        break
    else:
        res += tmp[0][1]
        last = tmp[0][0]

        if tmp[0][1] == 'L':
            lt += 1
        else:
            rt -= 1

        tmp.clear()

print(len(res))
print(res)