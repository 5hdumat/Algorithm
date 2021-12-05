# 내 문제풀이
n = int(input())
score_list = list(map(int, input().split()))
avg = round(sum(score_list) / n)
min = 2147483648

for index, value in enumerate(score_list):
    # 거리값 구하기
    tmp = abs(value - avg)

    if tmp < min:
        min = tmp
        score = value
        result = index + 1

    elif tmp == min and score < value:
        score = value
        result = index + 1

print(avg, result)

'''
위 코드는 오류가 있다.

파이썬에서의 round() 함수는 round_half_even 방식이다.
round_half_even의 경우 정확하게 4.50000과 같이 값이 정확히 하프 지점에 있다면 짝수 지점에 근사값을 지정한다.

예)
a = 4.500
print(round(a)) # 4

a = 4.5111
print(round(a)) # 5

round()가 아닌

a = 66.5
a = a+0.5
a = int(a) 와 같은 방식으로 사용해야 한다.
'''

# 오류 수정
n = int(input())
score_list = list(map(int, input().split()))
avg = int((sum(score_list) / n) + 0.5)
min = 2147483648

for index, value in enumerate(score_list):
    # 거리값 구하기
    tmp = abs(value - avg)

    if tmp < min:
        min = tmp
        score = value
        result = index + 1

    elif tmp == min and score < value:
        score = value
        result = index + 1

print(avg, result)

# 복습
n = int(input())
arr = list(map(int, input().split()))
avg = int((sum(arr) / n) + 0.5)

dis = 999999
res = 0
val = 0
for i in range(n):
    tmp = abs(avg - arr[i])

    if tmp < dis:
        dis = tmp
        val = arr[i]
        res = i + 1
    elif tmp == dis and arr[i] > val:
        val = arr[i]
        res = i + 1

print(avg, res)
