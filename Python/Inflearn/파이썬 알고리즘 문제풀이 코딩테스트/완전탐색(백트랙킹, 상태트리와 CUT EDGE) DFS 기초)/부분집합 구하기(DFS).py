'''
  입력값: 3 기준
  좌: 상단 노드 사용  /  우: 상단 노드 사용 안함
                d(1)
            /         \
          d(2)       d(2)
        /      \   /      \
    d(3)      d(3) d(3)   d(3)
   /    \    /   \ /   \  /   \
d(4) d(4) d(4) d(4) d(4) d(4) d(4) d(4)
'''


# def dfs(x):
#     if x == n + 1:  # x가 4번쨰 계층 노드일때 출력
#         for i in range(1, n+1):
#             if check[i] == 1:
#                 print(i, end=' ')
#         print()
#
#     else:
#         check[x] = 1  # 상단노드 사용 한다.
#         dfs(x + 1)
#         check[x] = 0  # 상단노드 사용 안한다.
#         dfs(x + 1)
#
#
# if __name__ == "__main__":
#     n = int(input())
#     check = [0] * (n + 1)
#     dfs(1)


# 복습

def DFS(x):
    if x > n:
        for i in range(1, n + 1):
            if ch[i] == 1:
                print(i, end=' ')
        print()

    else:
        ch[x] = 1
        DFS(x + 1)
        ch[x] = 0
        DFS(x + 1)


n = int(input())
ch = [0] * (n + 1)
DFS(1)
