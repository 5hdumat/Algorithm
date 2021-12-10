# https://www.acmicpc.net/problem/1182

def DFS(l, sum):
    global cnt

    if l == n:
        return

    if sum + a[l] == s:
        cnt += 1

    DFS(l + 1, sum + a[l])
    DFS(l + 1, sum)


n, s = map(int, input().split())
a = list(map(int, input().split()))
cnt = 0
DFS(0, 0)

print(cnt)
