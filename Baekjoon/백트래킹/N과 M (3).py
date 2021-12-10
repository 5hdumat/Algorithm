# https://www.acmicpc.net/problem/15651

n, m = map(int, input().split())

output = []

def dfs(depth):
    if depth == m: 
        print(*output) 
        return

    for i in range(n): 
        output.append(i + 1)
        dfs(depth + 1)
        output.pop()
            
dfs(0)

