'''
5 3
2 4 5 8 12
6
'''


def dfs(l, s):
    global cnt

    if l == k:
        if sum(res) % 6 == 0:
            cnt += 1
        return
    else:
        for i in range(s, n):
            if ch[i] == 0:
                ch[i] = 1
                res[l] = a[i]
                dfs(l + 1, i + 1)
                ch[i] = 0


n, k = map(int, input().split())
a = list(map(int, input().split()))
m = int(input())

res = [0] * k
ch = [0] * n
cnt = 0

dfs(0, 0)
print(cnt)