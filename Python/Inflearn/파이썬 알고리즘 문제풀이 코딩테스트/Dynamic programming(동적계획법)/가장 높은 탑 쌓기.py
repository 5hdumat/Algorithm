'''
5
25 3 4
4 4 6
9 2 3
16 2 5
1 5 2
'''
n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]
arr.sort(reverse=True)
dy = [0] * (n + 1)
dy[0] = arr[0][1]
res = 0
for i in range(1, n):
    tmp = 0
    for j in range(i - 1, -1, -1):  # 위에서 0부터 시작하므로 -1까지인거 주의
        if arr[i][2] < arr[j][2] and dy[j] > tmp:  # 기준이 되는 벽돌보다 비교군 벽돌이 더 커야한다. (여기서 기준 벽돌은 탑의 최상단에 놓여져있다.)
            tmp = dy[j]

    dy[i] = tmp + arr[i][1]
    res = max(res, dy[i])

print(res)
