import collections


def solution(money):
    if len(money) <= 3:
        return max(money)

    dp1 = [0] * len(money)
    dp2 = [0] * len(money)

    # 첫번째 집을 터는 경우
    dp1[0] = money[0]
    for i in range(1, len(money) - 1):  # 마지막 집 제외
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + money[i])

    # 첫번째 집을 안터는 경우
    dp2[0] = 0
    for j in range(1, len(money)):
        dp2[j] = max(dp2[j - 1], dp2[j - 2] + money[j])

    return max(dp1[i], dp2[j])


# 1 2 4 6
s = solution([1, 2, 3, 4, 14, 8])
# s = solution([2, 1, 3, 6])
# s = solution([0, 7, 3, 1, 0, 0, 0, 9])
