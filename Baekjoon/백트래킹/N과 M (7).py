# https://www.acmicpc.net/problem/15656

n, m = map(int, input().split())
number_list = list(map(int, input().split()))
number_list.sort()

output = []

def dfs(depth):
    if depth == m: 
        print(*output)
        return

    for i in range(n): 
        output.append(number_list[i])
        dfs(depth + 1)
        output.pop()
            
dfs(0)
