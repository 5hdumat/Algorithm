'''
5 3
1
2
8
4
9
'''

def Count(distance):
    cnt = 1
    end_point = Line[0]  # 말이 마지막에 배치된 지점

    for i in range(1, n):  # 첫번째 마굿간에 말이 이미 배치되어있으니 1부터 시작
        if Line[i] - end_point >= distance:
            cnt += 1
            end_point = Line[i]

    return cnt


n, c = map(int, input().split())
Line = []

for _ in range(n):
    Line.append(int(input()))

Line.sort()

lt = 1
rt = Line[n - 1]
res = 0
while lt <= rt:
    mid = (lt + rt) // 2 # 1, 9 // 1, 4 // 3, 4 // 4, 4
    if Count(mid) >= c:
        res = mid
        lt = mid + 1

    else:
        rt = mid - 1

print(res)
