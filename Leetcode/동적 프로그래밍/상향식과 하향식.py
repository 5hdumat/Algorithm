# 피보나치 문제로 상향식과 하향식 이해하기

# 상향식 (타뷸레이션, 하위 문제부터 차례대로 정답을 풀어나가며 큰 문제의 정답을 만든다.)
import collections

dp = collections.defaultdict(list)


def bottom_up(n):
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    print(dp[n])


bottom_up(5)

# 하향식 (메모이제이션, 하위 문제에 대한 정답을 계산했는지 확인해가며 문제를 재귀로 풀어나가는 방식)
dp = collections.defaultdict(list)


def top_down(n):
    if n <= 1:
        return n

    if dp[n]:
        return dp[n]

    dp[n] = top_down(n - 1) + top_down(n - 2)
    return dp[n]


top_down(5)
