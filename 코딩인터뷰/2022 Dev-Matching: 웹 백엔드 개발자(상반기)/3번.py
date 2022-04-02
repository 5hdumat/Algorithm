import copy


def solution(grid):
    answer = 0

    for alpha in ['a','b','c']:
        tmp = copy.deepcopy(grid)

        print(tmp)

    return answer


solution(["??b", "abc", "cc?"])
