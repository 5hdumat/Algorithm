# https://www.acmicpc.net/problem/15655

n, m = map(int, input().split())
number_list = list(map(int, input().split()))
number_list.sort()

visited = [False] * n
output = []

def dfs(depth, idx):
    if depth == m: 
        print(*output) 
        return

    for i in range(idx, n): 
        if not visited[i]:
            visited[i] = True
            
            output.append(number_list[i])
            dfs(depth + 1, i)
            
            visited[i] = False
            output.pop()
            
dfs(0, 0)
