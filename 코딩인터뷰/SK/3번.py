import math


def solution(width, height, diagonals):
    tables = [[0] * (height + 1) for _ in range(width + 1)]

    for i, table in enumerate(tables):
        for j, row in enumerate(table):
            if i == 0 or j == 0:
                tables[i][j] = 1
            else:
                tables[i][j] = tables[i - 1][j] + tables[i][j - 1]

    answer = 0

    for dx, dy in diagonals:
        answer += tables[dx - 1][dy] * tables[width - dx][height - dy + 1]
        answer += tables[dx][dy - 1] * tables[width - dx + 1][height - dy]

    print(int(answer % 10000019))


solution(2, 2, [[1, 1], [2, 2]])
solution(3, 2, [[1, 2], [3, 2], [3, 1]])
solution(51, 37, [[17, 19]])
