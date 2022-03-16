def solution(n, computers):
    def _dfs(l):
        if visited[l]:
            return

        visited[l] = True

        for index, node in enumerate(computers[l]):
            # 1. 노드 레벨이 나 자신이 아니면서, (l != index)
            # 2. 방문한 적이 없고, (not visited[index])
            # 3. 연결된 상태여야 한다. (node == 1)
            if l != index and node == 1 and not visited[index]:
                _dfs(index)

    visited = [False] * n

    answer = 0
    for i in range(n):
        # 연결 된 상태의 컴퓨터라면 한번의 DFS로 두 컴퓨터가 방문처리된다.
        if not visited[i]:
            answer += 1
            _dfs(i)

    return answer


solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])
