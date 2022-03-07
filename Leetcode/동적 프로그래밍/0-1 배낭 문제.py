cargo = [
    (4, 12),
    (2, 1),
    (10, 4),
    (1, 1),
    (2, 2)
]


def zero_one_knapsack(cargo):
    capacity = 15
    pack = []

    # 6 x 16 테이블 생성 (짐 개수 + 1 x 배낭용량 + 1)
    for i in range(len(cargo) + 1):
        pack.append([])
        for c in range(capacity + 1):
            if i == 0 or c == 0:
                pack[i].append(0)
            elif cargo[i - 1][1] <= c:
                pack[i].append(
                    max(
                        cargo[i - 1][0] + pack[i - 1][c - cargo[i - 1][1]],
                        pack[i - 1][c]
                    ))
            else:
                pack[i].append(pack[i - 1][c])

    print(pack[-1][-1])


r = zero_one_knapsack(cargo)
