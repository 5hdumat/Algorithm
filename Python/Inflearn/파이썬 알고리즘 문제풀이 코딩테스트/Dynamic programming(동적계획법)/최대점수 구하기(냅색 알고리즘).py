'''
5 20
10 5
25 12
15 8
6 3
7 4
'''

# 2차원 해결법 (시간복잡도 높음)
if __name__ == '__main__':
    n, m = map(int, input().split())
    dy = [[0] * (m + 1) for _ in range(n + 2)]

    for i in range(1, n + 1):
        score, time = map(int, input().split())

        for j in range(time, m + 1):
            tmp = max(dy[i - 1][j - time] + score, dy[i][j])
            dy[i][j] = tmp

            # 다음줄에 미리 복사해놓기
            dy[i + 1][j] = tmp

# for x in dy:
#     print(x)

print(dy[n + 1][-1])

# 1차원 해결법 (시간복잡도 낮음)
if __name__ == '__main__':
    n, m = map(int, input().split())
    dy = [0] * (m + 1)

    for i in range(1, n + 1):
        score, time = map(int, input().split())

        for j in range(m, time - 1, -1):
            dy[j] = max(dy[j - time] + score, dy[j])

print(dy[-1])

# 강의 문제 풀이
if __name__ == '__main__':
    n, m = map(int, input().split())
    dy = [0] * (m + 1)

    for i in range(n):
        ps, pt = map(int, input().split())

        for j in range(m, pt - 1, -1):
            dy[j] = max(dy[j], dy[j - pt] + ps)

print(dy[m])
