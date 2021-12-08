# '''
# 2 4 1 5 3 2 6
# 3 5 1 8 7 1 7
# 8 3 2 7 1 3 8
# 6 1 2 3 2 1 1
# 1 3 1 3 5 3 2
# 1 1 2 5 6 5 2
# 1 2 2 2 2 1 5
# '''
# # 내 문제풀이
# a = [list(map(int, input().split())) for _ in range(7)]
# res = 0
#
# for i in range(7):
#     for j in range(3):
#         check1 = []
#         check2 = []
#         for k in range(5):
#             check1.append(a[i][j + k]) # 행
#             check2.append(a[j + k][i]) # 열
#
#         if check1 == check1[::-1]:
#             res += 1
#
#         if check2 == check2[::-1]:
#             res += 1
#
# print(res)
#
# # 문제풀이 개선
# a = [list(map(int, input().split())) for _ in range(7)]
# res = 0
#
# for i in range(7):
#
#     s = 0
#     for _ in range(3):
#         # 행
#         if a[i][s] == a[i][s+4] and a[i][s+1] == a[i][s+3]:
#             res += 1
#
#         # 열
#         if a[s][i] == a[s+4][i] and a[s+1][i] == a[s+3][i]:
#             res += 1
#
#         s += 1
#
# print(res)
#
# # 강의 문제 풀이
# board = [list(map(int, input().split())) for _ in range(7)]
# cnt = 0
#
# for i in range(3):
#     for j in range(7):
#         tmp = board[j][i:i+5]
#
#         if tmp == tmp[::-1]:
#             cnt += 1
#
#         for k in range(2):
#             if board[i+k][j] != board[i+4-k][j]:
#                 break
#         else:
#             cnt += 1
#
# print(cnt)
#


'''
2 4 1 5 3 2 6
3 5 1 8 7 1 7
8 3 2 7 1 3 8
6 1 2 3 2 1 1
1 3 1 3 5 3 2
1 1 2 5 6 5 2
1 2 2 2 2 1 5
'''
# 복습

board = [list(map(int, input().split())) for _ in range(7)]
cnt = 0

for i in range(7):

    s = 0
    for j in range(3):

        # 행
        if board[i][s] == board[i][s + 4] and board[i][s + 1] == board[i][s + 3]:
            cnt += 1

        # 열
        if board[s][i] == board[s + 4][i] and board[s + 1][i] == board[s + 3][i]:
            cnt += 1

        s += 1

print(cnt)
