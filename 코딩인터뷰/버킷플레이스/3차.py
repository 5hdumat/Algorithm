import collections


def solution(tstring, variables):
    graph = collections.defaultdict(str)
    for variable in variables:
        graph['{' + variable[0] + '}'] = variable[1]

    # for i, v in graph.copy().items():
    #     if graph[v].isalpha():
    #         graph[i] = graph[v]
    #
    for _ in range(2):
        for i, v in graph.copy().items():
            if v != '':
                tstring = tstring.replace(i, v)


    print(tstring)

    return tstring


solution("this is {template} {template} is {state}", [["template", "string"], ["state", "{template}"]])
solution("this is {template} {template} is {state}", [["template", "{state}"], ["state", "{template}"]])
solution("this is {template} {template} is {state}", [["template", "{state}"], ["state", "{template}"]])
solution("this is {template} {template} is {state}", [["template", "{state}"], ["state", "{templates}"]])
solution("{a} {b} {c} {d} {i}",
         [["b", "{c}"], ["a", "{b}"], ["e", "{f}"], ["h", "i"], ["d", "{e}"], ["f", "{d}"], ["c", "d"]])
