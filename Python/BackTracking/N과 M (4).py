# https://www.acmicpc.net/problem/15652

n, m = map(int, input().split())

output = []

def dfs(depth, idx):
    if depth == m:
        return

    for i in range(idx, n): 
        output.append(i + 1)
        dfs(depth + 1, i)
        output.pop()
            
dfs(0, 0)

