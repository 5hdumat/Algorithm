def solution(n, computers):
    def _stack(l):
        if visited[l]:
            return

        visited[l] = True
        stack = [l]

        while stack:
            pop = stack.pop()

            for i, node in enumerate(computers[l]):
                if i != pop and computers[pop][i] == 1 and not visited[i]:
                    visited[i] = True
                    stack.append(i)

    answer = 0
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            answer += 1
            _stack(i)

    return answer


solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])
