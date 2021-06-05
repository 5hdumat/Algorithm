# https://www.acmicpc.net/problem/15652

n, m = map(int, input().split())

visited = [False] * n
output = []

def dfs(depth, idx):
    if depth == m: # 탈출 조건
        print(*output) # *: list Unpacking 후 출력
        return

    for i in range(idx, n): 
        output.append(i + 1)
        dfs(depth + 1, i)
        output.pop()
            
dfs(0, 0)

