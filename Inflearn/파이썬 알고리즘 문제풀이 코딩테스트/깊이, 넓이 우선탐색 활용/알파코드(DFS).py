def dfs(L, P):
    global cnt

    if L == n:
        cnt += 1

        for i in range(P):
            print(chr(res[i]+64), end='')

        print()
    else:
        for i in range(1, 27):
            if i == code[L]:
                res[P] = i
                dfs(L + 1, P + 1)

            if i >= 10 and code[L] == i // 10 and code[L + 1] == i % 10:
                res[P] = i
                dfs(L + 2, P + 1)


if __name__ == "__main__":
    code = list(map(int, input()))
    n = len(code)
    code.insert(n, -1)
    res = [0] * (n + 3)
    cnt = 0
    dfs(0, 0)
    print(cnt)
