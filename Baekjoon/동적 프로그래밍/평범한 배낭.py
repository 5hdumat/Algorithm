n, k = map(int, input().split())

cargo = []

for _ in range(n):
    w, v = map(int, input().split())
    cargo.append((w, v))


# 타뷸레이션 구현
def tabulation(cargo):
    capacity = k
    pack = []

    for i in range(len(cargo) + 1):
        pack.append([])
        for c in range(capacity + 1):
            if i == 0 or c == 0:
                pack[i].append(0)
            elif cargo[i - 1][0] <= c:
                pack[i].append(max(
                    cargo[i - 1][1] + pack[i - 1][c - cargo[i - 1][0]],
                    pack[i - 1][c]
                ))
            else:
                pack[i].append(pack[i - 1][c])

    print(pack[-1][-1])


tabulation(cargo)
