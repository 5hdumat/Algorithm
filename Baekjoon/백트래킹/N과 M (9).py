# https://www.acmicpc.net/problem/15663

n, m = map(int, input().split())
number_list = list(map(int, input().split()))
number_list.sort()

visited = [False] * n
temp_list = []
output = []

def dfs(depth):
    if depth == m: 
        if not tuple(temp_list) in output:
            output.append(tuple(temp_list))
            return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            
            temp_list.append(number_list[i])
            dfs(depth + 1)
            
            visited[i] = False
            temp_list.pop()
            
dfs(0)

for i in output:
    print(*i)
   
# set을 사용해 hash를 이용한 시간 초과 개선  
# https://www.acmicpc.net/problem/15663

n, m = map(int, input().split())
number_list = list(map(int, input().split()))
number_list.sort()

visited = [False] * n
temp_list = []
output = []

def dfs(depth):
    if depth == m: 
        output.append(tuple(temp_list))
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            
            temp_list.append(number_list[i])
            dfs(depth + 1)
            
            visited[i] = False
            temp_list.pop()
            
dfs(0)

output = list(set(output))

output.sort()

for i in output:
    print(*i)

# 시간초과로 계속 실패 이후 개선
n, m = list(map(int, input().split()))

number_list = list(map(int, input().split()))
number_list.sort()

visited = [False] * n 
output = []

def dfs(depth):
    if depth == m:
        print(*output)
        return
    
    overlap = 0
    for i in range(n):
        if not visited[i] and overlap != number_list[i]:
            visited[i] = True
            
            output.append(number_list[i])
            overlap = number_list[i]
            
            dfs(depth + 1)
            visited[i] = False
            output.pop()
        
dfs(0)
