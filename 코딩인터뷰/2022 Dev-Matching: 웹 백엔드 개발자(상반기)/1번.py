import sys


def solution(dist):
    tmp_list = []
    max_value = max(map(max, dist))
    for i in range(len(dist)):
        for j in range(len(dist)):
            if dist[i][j] == max_value:
                tmp_list.append(i)

        if tmp_list:
            break

    i = tmp_list[0]
    while len(tmp_list) < len(dist):
        tmp = sys.maxsize
        for i, v in enumerate(dist[i]):
            if v == 0:
                continue

            if v < tmp and i not in tmp_list:
                min_idx = i
                tmp = min(tmp, v)

        tmp_list.append(min_idx)
        i = tmp_list[-1]

    return sorted([tmp_list, tmp_list[::-1]])


solution([[0, 5, 2, 4, 1], [5, 0, 3, 9, 6], [2, 3, 0, 6, 3], [4, 9, 6, 0, 3], [1, 6, 3, 3, 0]])
