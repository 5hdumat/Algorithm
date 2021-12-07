'''
5
10 13 10 12 15
12 39 30 23 11
11 25 50 53 15
19 27 29 37 27
19 13 30 13 19
'''

# 내 문제풀이
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
sum3 = sum4 = 0
largest = -2147000000

for i in range(n):
    sum1 = sum2 = 0

    for j in range(n):
        sum1 += a[i][j]
        sum2 += a[j][i]

    sum3 += a[i][i]
    sum4 += a[i][n - i - 1]

    if largest < sum1:
        largest = sum1

    if largest < sum2:
        largest = sum2

    if largest < sum3:
        largest = sum3

    if largest < sum4:
        largest = sum4

print(largest)

# 강의 문제 풀이
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
largest = -2147000000

for i in range(n):
    sum1 = sum2 = 0

    for j in range(n):
        sum1 += a[i][j]
        sum2 += a[j][i]

        if largest < sum1:
            largest = sum1

        if largest < sum2:
            largest = sum2

sum1 = sum2 = 0

for i in range(n):
    sum1 += a[i][i]
    sum2 += a[i][n - i - 1]

if largest < sum1:
    largest = sum1

if largest < sum2:
    largest = sum2

print(largest)

# 복습

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
largest = 0
for i in range(n):
    sum1 = sum2 = 0

    for j in range(n):
        sum1 += arr[i][j]
        sum2 += arr[j][i]

    if largest < sum1:
        largest = sum1

    if largest < sum2:
        largest = sum2

sum1 = sum2 = 0

for i in range(n):
    sum1 += arr[i][i]
    sum2 += arr[i][n - i - 1]

    if largest < sum1:
        largest = sum1

    if largest < sum2:
        largest = sum2

print(largest)
