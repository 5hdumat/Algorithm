# https://www.acmicpc.net/problem/11723

import sys

n = int(input())

visited = [False] * 20    
        
for _ in range(n):
    tmp = sys.stdin.readline().split()
    
    type = tmp[0]
    if len(tmp) > 1:
        x = int(tmp[1]) - 1
    
    if type == 'add': # add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
        if not visited[x]:
            visited[x] = True
    elif type == 'remove': # remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
        if visited[x]:
            visited[x] = False
    elif type == 'check': # check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
        if visited[x]:
            print(1)
        else:
            print(0)
    elif type == 'toggle': # toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
        if visited[x]:
            visited[x] = False
        else:
            visited[x] = True
    elif type == 'all': # all: S를 {1, 2, ..., 20} 으로 바꾼다.
        visited = [True] * 20
    else: # empty: S를 공집합으로 바꾼다. 
        visited = [False] * 20
        


# 리스트로 해결 했지만.. set()을 사용한 정석 문제 풀이
import sys

n = int(input())
s = set()

for _ in range(n):
    tmp = sys.stdin.readline().strip().split()
    
    type = tmp[0]
    if len(tmp) > 1:
        x = int(tmp[1]) 
    
    if type == 'add':
        s.add(x)
    elif type == 'check':
        print(1 if x in s else 0) # if in else : one line
    elif type == 'remove':
        s.discard(x)
    elif type == 'toggle':
        s.discard(x) if x in s else s.add(x)
    elif type == 'all':
        s = set(range(1, 21))
    else:
        s = set()
    
    
    