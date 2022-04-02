from itertools import product


def solution(grid):
    answer = -1

    repeat = 0
    for x in grid:
        repeat += x.count('?')

    # for x in list(product(['a', 'b', 'c'], repeat=repeat)):
    #     print(x)

    return answer


solution(["??b", "abc", "cc?"])
solution(["abcabcab", "????????"])
solution(["aa?"])
