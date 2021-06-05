# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
# https://www.acmicpc.net/problem/15649

n, m = map(int, input().split())

number_list = [1 + i for i in range(n)]
list = []

def dfs():
    if len(list) == m:
        print(*list) 
        return

    for i in number_list: 
        if not i in list:
            list.append(i)
            dfs()
            list.pop()
             
dfs()

# 외장함수 permutations을 이용한 방법
from itertools import permutations

n, m = map(int, input().split())

list = [i + 1 for i in range(n)]

for i in permutations(list, m):
    print(*i)