# https://www.acmicpc.net/problem/15654

n, m = map(int, input().split())
number_list = list(map(int, input().split()))
number_list.sort()

visited = [False] * n
output = []

def dfs(depth):
    if depth == m: # 탈출 조건
        print(*output) # *: list Unpacking 후 출력
        return

    for i in range(n): 
        if not visited[i]:
            visited[i] = True
            
            output.append(number_list[i])
            dfs(depth + 1)
            
            visited[i] = False
            output.pop()
            
dfs(0)
