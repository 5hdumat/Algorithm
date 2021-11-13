'''
(사전지식) 무방향 그래프

입력예시
5 5
1 2
1 3
2 4
3 4
4 5
'''

# n, m = map(int, input().split())
# g = [[0] * (n + 1) for _ in range(n + 1)]
#
# for i in range(m):
#     a, b = map(int, input().split())
#
#     g[a][b] = 1
#     g[b][a] = 1
#
# for x in g:
#     print(x)

'''
(문제) 가중치 방향 그래프

입력예시
6 9 
1 2 7 
1 3 4 
2 1 2 
2 3 5 
2 5 5 
3 4 5 
4 2 2 
4 5 5 
6 4 5
'''

n, m = map(int, input().split())
g = [[0] * n for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())

    g[a-1][b-1] = c

for x in g:
    print(*x)