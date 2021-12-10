'''
5 9
1 2
1 3
1 4
2 1
2 3
2 5
3 4
4 2
4 5
'''


def dfs(v):
    global cnt

    if v == n - 1:
        cnt += 1
    else:
        for i in range(n):
            # v에서 i로 이동할 수 있는 간선이 있는가?
            if g[v][i] == 1 and ch[i] == 0:
                ch[i] = 1
                dfs(i)  # 있다면 i를 인자로 넘긴다.
                ch[i] = 0


n, m = map(int, input().split())
g = [[0] * n for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    g[a - 1][b - 1] = 1

cnt = 0
ch = [0] * n
ch[0] = 1  # 시작하는 노드는 이미 방문해있는 상태

dfs(0)
print(cnt)


# 경로 출력해보기

def dfs(v):
    global cnt

    if v == n - 1:
        print(*path)
    else:
        for i in range(n):
            # v에서 i로 이동할 수 있는 간선이 있는가?
            if g[v][i] == 1 and ch[i] == 0:
                ch[i] = 1
                path.append(i + 1)
                dfs(i)  # 있다면 i를 인자로 넘긴다.
                path.pop()
                ch[i] = 0


n, m = map(int, input().split())
g = [[0] * n for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    g[a - 1][b - 1] = 1

cnt = 0
ch = [0] * n

ch[0] = 1  # 시작하는 노드는 이미 방문해있는 상태
path = []
path.append(1)

dfs(0)
