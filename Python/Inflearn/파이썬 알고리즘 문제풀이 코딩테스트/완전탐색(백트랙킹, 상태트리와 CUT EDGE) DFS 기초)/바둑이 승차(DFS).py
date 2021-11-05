'''
259 5
81
58
42
33
61
'''


def dfs(level, sum):
    if sum > c:
        return

    if level == n:
        global max_weight

        if sum > max_weight:
            max_weight = sum

        return
    else:
        dfs(level + 1, sum + a[level])  # 바둑이를 태우는 케이스
        dfs(level + 1, sum)  # 바둑이를 태우지 않는 케이스


if __name__ == "__main__":
    c, n = map(int, input().split())
    a = []
    for _ in range(n):
        a.append(int(input()))

    total = sum(a)
    max_weight = 0

    dfs(0, 0)

    print(max_weight)


# 강의 문제 풀이
def dfs(L, sum, total_sum):
    global result

    print(sum, total_sum, result, (total_dog_weight - total_sum), end= ' // ')
    # 가지 치기
    if sum + (total_dog_weight - total_sum) < result:
        return

    if sum > c:
        return
    print(L, n)
    if L == n:
        if sum > result:
            result = sum
    else:
        dfs(L + 1, sum + a[L], total_sum+a[L])
        dfs(L + 1, sum, total_sum+a[L])


if __name__ == "__main__":
    c, n = map(int, input().split())
    a = []

    for _ in range(n):
        a.append(int(input()))

    result = -2147000000
    total_dog_weight = sum(a)
    total_sum = 0

    dfs(0, 0, 0)

    print(result)