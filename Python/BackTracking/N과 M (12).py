# https://www.acmicpc.net/problem/15666

n, m = list(map(int, input().split()))

number_list = list(map(int, input().split()))
number_list.sort()

visited = [False] * n 
output = []

def dfs(depth, idx):
    if depth == m:
        print(*output)
        return
    
    overlap = 0
    for i in range(idx, n):
        if overlap != number_list[i]:
            output.append(number_list[i])
            overlap = number_list[i]
            
            dfs(depth + 1, i)
            output.pop()
        
dfs(0, 0)