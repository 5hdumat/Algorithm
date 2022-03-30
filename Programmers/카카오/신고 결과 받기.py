import collections


def solution(id_list, report, k):
    answer = [0] * len(id_list)

    graph = collections.defaultdict(list)
    for x in report:
        reporter, attacker = x.split()
        if reporter not in graph[attacker]:
            graph[attacker].append(reporter)

    for attacker, reporter in graph.items():
        if len(reporter) >= k:
            for x in reporter:
                answer[id_list.index(x)] += 1

    return answer

solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2)
solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 2)
