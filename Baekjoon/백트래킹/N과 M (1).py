# https://www.acmicpc.net/problem/15649

# 첫번째 문제풀이 
n, m = map(int, input().split())

number_list = [1 + i for i in range(n)]
output = []

def dfs():
    if len(output) == m:
        print(*output) 
        return

    for i in number_list: 
        if not i in output:
            output.append(i)
            dfs()
            output.pop()
             
dfs()

# 성능 개선 문제풀이 (선형 탐색 시간 배제)
n, m = map(int, input().split())

visited = [False] * n
output = []

def dfs(depth):
    if depth == m: # 탈출 조건
        print(*output) # *: list Unpacking 후 출력
        return

    for i in range(n): 
        if not visited[i]:
            visited[i] = True

            output.append(i + 1)
            dfs(depth + 1)
            
            visited[i] = False
            output.pop()
             
dfs(0)

# 외장함수 permutations을 이용한 방법
from itertools import permutations

n, m = map(int, input().split())

for i in permutations(range(1, n + 1), m):
    print(*i)