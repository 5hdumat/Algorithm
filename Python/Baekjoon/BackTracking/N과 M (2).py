# https://www.acmicpc.net/problem/15650

n, m = map(int, input().split())

visited = [False] * n
output = []

def dfs(depth, idx):
    if depth == m:
        print(*output)
        return
    
    for i in range(idx, n):
        if not visited[i]: 
            visited[i] = True 
            
            output.append(i+1) 
            dfs(depth + 1, i + 1) 
            
            visited[i] = False
            output.pop()
            
dfs(0, 0)
    
# 내장함수 combinations을 이용한 방법
    
from itertools import combinations

n, m = map(int, input().split())

for i in combinations(range(1, n + 1), m):
    print(*i)