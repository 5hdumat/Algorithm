def solution(board, moves):
    answer = 0
    bucket = []

    for x in moves:
        y = 0
        while y < len(board) - 1 and board[y][x - 1] == 0:
            y += 1

        if board[y][x - 1] == 0:
            continue

        bucket.append(board[y][x - 1])

        while True:
            if len(bucket) >= 2 and bucket[-1] == bucket[-2]:
                bucket.pop()
                bucket.pop()

                answer += 2
            else:
                break

        board[y][x - 1] = 0

    return answer


solution([[5, 5, 5, 5, 5], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]],
         [1, 5, 3, 5, 1, 2, 1, 4])

solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]],
         [1, 5, 3, 5, 1, 2, 1, 4])

solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]],
         [1, 5, 3, 5, 1, 2, 1, 4])
