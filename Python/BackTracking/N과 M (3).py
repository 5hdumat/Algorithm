# https://www.acmicpc.net/problem/15651

n, m = map(int, input().split())

visited = [False] * n
output = []

def dfs(depth):
    if depth == m: # 탈출 조건
        print(*output) # *: list Unpacking 후 출력
        return

    for i in range(n): 
        output.append(i + 1)
        dfs(depth + 1)
        output.pop()
            
dfs(0)

