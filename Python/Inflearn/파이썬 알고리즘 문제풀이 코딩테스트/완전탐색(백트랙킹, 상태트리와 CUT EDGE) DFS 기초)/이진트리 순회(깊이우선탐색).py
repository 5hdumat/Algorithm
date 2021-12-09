# # 전위 순위 출력
# def dfs(v):
#     if v > 7:
#         return
#     else:
#         print(v, end=' ')
#         dfs(v * 2)
#         dfs(v * 2 + 1)
#
#
# if __name__ == "__main__":
#     dfs(1)
#
#
# print()
#
# # 중위 순위 출력
# def dfs(v):
#     if v > 7:
#         return
#     else:
#         dfs(v * 2)
#         print(v, end=' ')
#         dfs(v * 2 + 1)
#
#
# if __name__ == "__main__":
#     dfs(1)
#
# print()
#
#
# # 후위 순위 출력 (병합정렬에서 쓰임)
# def dfs(v):
#     if v > 7:
#         return
#     else:
#         dfs(v * 2)
#         dfs(v * 2 + 1)
#         print(v, end=' ')
#
#
# if __name__ == "__main__":
#     dfs(1)


def DFS(x):
    if x > 7:
        return

    # 전위
    # print(x, end='')

    DFS(x * 2) # 1에서 2로

    # 중위
    # print(x, end='') # 1에서 3으로

    DFS(x * 2 + 1)
    
    # 후위
    print(x, end='')


DFS(1)
