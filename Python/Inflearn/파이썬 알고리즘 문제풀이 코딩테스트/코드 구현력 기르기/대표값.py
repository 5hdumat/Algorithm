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

