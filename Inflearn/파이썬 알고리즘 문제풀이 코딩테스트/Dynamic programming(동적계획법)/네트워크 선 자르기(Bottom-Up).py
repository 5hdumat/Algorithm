n = int(input())
dy = [0] * (n + 1)

# 직관적으로 알 수 있는 것은 그냥 초기화해놓기
dy[1] = 1
dy[2] = 2

for i in range(3, n + 1):
    dy[i] = dy[i-1] + dy[i-2]

print(dy[n])
print(dy)