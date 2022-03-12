def solution(m, n, board):
    board = [list(x) for x in board]

    matched = []
    while True:
        for i in range(m - 1):
            for j in range(n - 1):
                if board[i][j] == board[i][j + 1] == board[i + 1][j] == board[i + 1][j + 1] != '#':
                    matched.append((i, j))

        if not matched:
            break

        for _ in range(len(matched)):
            x, y = matched.pop(0)
            board[x][y] = board[x][y + 1] = board[x + 1][y] = board[x + 1][y + 1] = '#'

        # 맨위에있는 프렌즈 블럭을 맨밑으로 내리고
        # 위아래로 프렌즈 블럭이 있을 경우를 대비해 다시 한번 맨위에서부터 반복적으로 체크해서 블럭을 내려야 한다.
        for _ in range(m - 1):
            for i in range(m - 1):
                for j in range(n):
                    if board[i][j] != '#' and board[i + 1][j] == '#':
                        board[i][j], board[i + 1][j] = '#', board[i][j]

    return sum([x.count('#') for x in board])

# 높이, 폭, 배치 정보
solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"])
