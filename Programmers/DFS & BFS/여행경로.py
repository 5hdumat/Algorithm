import collections


def solution(tickets):
    def _dfs(course):
        # 주의) if로 하면 해당 코스에서 경로가 끝길 경우를 대비하지 못함

        # {'SFO': ['ATL'], 'ICN': ['ICN', 'ATL'], 'ATL': ['SFO', 'ICN']}
        # ICN(출발) -> ATL -> ICN -> ICN = bad

        # ICN -> ICN -> SFO (ATL에서 while문을 통해 SFO로 넘어감) -> ATL -> ICN
        # 이 순서로 백트래킹
        while graph[course]:
            _dfs(graph[course].pop())

        answer.append(course)

    graph = collections.defaultdict(list)

    for sta, des in sorted(tickets, reverse=True):
        graph[sta].append(des)

    print(graph)
    answer = []
    _dfs('ICN')
    print(answer[::-1])
    return answer[::-1]


# s = solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]])
s = solution([["ICN", "ICN"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]])
