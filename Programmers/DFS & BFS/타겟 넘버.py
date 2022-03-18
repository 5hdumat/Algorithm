def solution(numbers, target):
    def _dfs(l, s):
        nonlocal answer

        if l == len(numbers):
            if s == target:
                answer += 1

            return

        _dfs(l + 1, s + numbers[l])
        # print(l, s + numbers[l])
        _dfs(l + 1, s - numbers[l])

    answer = 0
    _dfs(0, 0)
    return answer


solution([1, 1, 1, 1, 1], 3)
# solution([4, 1, 2, 1], 4)
