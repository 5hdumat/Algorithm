import collections


def solution(orders, course):
    def _dfs(l, s):
        if len(tmp) in course:
            arr[''.join(sorted(tmp))] += 1

        if l == len(order):
            return

        for i in range(s, len(order)):
            tmp.append(order[i])
            _dfs(l + 1, i + 1)
            tmp.pop()

    arr = collections.defaultdict(int)
    for order in orders:
        tmp = []
        _dfs(0, 0)

    # 최대 주문수 기록 (동일한 갯수의 코스요리임에도 주문수가 적으면 거르기 위함)
    max_graph = [0] * (course[-1] + 1)

    for k, v in arr.items():
        max_graph[len(k)] = max(max_graph[len(k)], v)

    answer = []
    for k, v in arr.items():
        if max_graph[len(k)] == v and v > 1:
            answer.append(k)

    return sorted(answer)


solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4])
solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5])
solution(["XYZ", "XWY", "WXA"], [2, 3, 4])
