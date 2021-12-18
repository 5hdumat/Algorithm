def move(no, x, y):
    if n == 1:
        res.append((x, y))
        return

    if no > 1:
        move(no - 1, x, 6 - x - y)

    res.append((x, y))

    if no > 1:
        move(no - 1, 6 - x - y, y)


n = int(input())

if n <= 20:
    res = []
    move(n, 1, 3)

    print((2 ** n) - 1)
    for x, y in res:
        print(f'{x} {y}')
else:
    # 이동 횟수 2**n-1
    print((2 ** n) - 1)
