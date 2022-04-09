import collections
from collections import deque


def solution(path):
    answer = []

    graph = {
        'NW': 'left',
        'NE': 'right',
        'WS': 'left',
        'WN': 'right',
        'EN': 'left',
        'ES': 'right',
        'SE': 'left',
        'SW': 'right'
    }

    dict = collections.defaultdict(str)
    for i, v in enumerate(path):
        dict[i] = v

    go = 0
    for i, v in enumerate(path):
        if i - 1 < 0:
            go += 1

        elif dict[i - 1] == dict[i]:
            go += 1
        else:

            print(go, (go / 5))
            go = 1



    return answer


# solution("EEESEEEEEENNNN")
solution("SSSSSSWWWNNNNNN")
solution("SSSSSSSSSSSSSSSSWWWNNNNNN")
