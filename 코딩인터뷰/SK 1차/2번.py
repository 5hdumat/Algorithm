def solution(n, clockwise):
    graph = [[0] * n for _ in range(n)]

    def _dfs(num=1, first=0, last=n - 1):
        # 각 꼭짓점에 값 세팅
        graph[first][first] = num
        graph[first][last] = num
        graph[last][first] = num
        graph[last][last] = num

        middle = [x for x in range(num + 1, (num + 1) + (last - first - 2) + 1)]

        if not middle:
            return

        if not clockwise:
            middle.sort(reverse=True)

        start = max(middle) + 1

        fill = [x for x in range(first + 1, last)]

        for m, a in enumerate(fill):
            fill_index = n - a - 1

            graph[first][a] = middle[m]
            graph[a][last] = middle[m]
            graph[last][fill_index] = middle[m]
            graph[fill_index][first] = middle[m]

        _dfs(start, first + 1, last - 1)

    _dfs()

    return graph


solution(5, True)
