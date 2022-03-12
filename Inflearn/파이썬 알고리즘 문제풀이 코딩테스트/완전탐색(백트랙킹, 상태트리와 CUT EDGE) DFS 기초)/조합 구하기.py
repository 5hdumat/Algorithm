def dfs(l, s):
    global cnt

    if l == m:
        cnt += 1
        print(*res)
        return
    else:
        for i in range(s, n + 1):
            if ch[i] == 0:
                ch[i] = 1
                res[l] = i
                dfs(l + 1, i + 1)
                ch[i] = 0


n, m = map(int, input().split())
res = [0] * m
ch = [0] * (n + 1)
cnt = 0
dfs(0, 0)
print(cnt)
