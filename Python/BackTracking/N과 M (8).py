# https://www.acmicpc.net/problem/15657

n, m = map(int, input().split())
number_list = list(map(int, input().split()))
number_list.sort()

output = []

def dfs(depth, idx):
    if depth == m: 
        print(*output) 
        return

    for i in range(idx, n): 
        output.append(number_list[i])
        dfs(depth + 1, i)
        output.pop()
            
dfs(0, 0)
