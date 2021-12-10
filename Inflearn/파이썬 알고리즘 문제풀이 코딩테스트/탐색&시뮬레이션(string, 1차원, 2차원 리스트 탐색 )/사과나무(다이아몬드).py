'''
5
10 13 10 12 15
12 39 30 23 11
11 25 50 53 15
19 27 29 37 27
19 13 30 13 19
'''

# 강의 문제 풀이
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
s = e = n // 2
apple = 0

for i in range(n):
    print(i)
    for j in range(s, e + 1):
        apple += a[i][j]  # (0) 0 2 //(1)  1 1, 1 2, 1 3 //(2)  2 0, 2 1, 2 2, 2 3, 2 4 //(3)  3 1, 3 2, 3 4 //(4)  4 2
        print(i, j)

    if i < n // 2:  # (0) 1 3 // (1)  0 4 // (2)  1 3 // (3)  2 2
        s -= 1
        e += 1
    else:
        s += 1
        e -= 1

print(apple)

# 복습
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

lt = rt = n // 2
apple = 0
for i in range(n):
    apple += sum(arr[i][lt:rt + 1])
    if i < n // 2:
        lt -= 1
        rt += 1

    else:
        lt += 1
        rt -= 1

print(apple)
