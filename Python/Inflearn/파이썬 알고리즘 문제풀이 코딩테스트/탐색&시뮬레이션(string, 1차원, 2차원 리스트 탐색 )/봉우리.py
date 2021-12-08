# '''
# 5
# 5 3 7 2 3
# 3 7 1 6 1
# 7 2 5 3 4
# 4 3 6 4 1
# 8 7 3 5 2
# '''
# # 내 문제 풀이
# n = int(input())
# a = [list(map(int, input().split())) for _ in range(n)]
#
# a.insert(0, [0] * n)
# a.append([0] * n)
#
# for x in a:
#     x.insert(0, 0)
#     x.append(0)
#
# cnt = 0
#
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         spot = a[i][j]
#
#         if a[i - 1][j] < spot and a[i + 1][j] < spot and a[i][j - 1] < spot and a[i][j + 1] < spot:
#             cnt += 1
#
# print(cnt)
#
# # 강의 문제 풀이
# n = int(input())
# a = [list(map(int, input().split())) for _ in range(n)]
#
# a.insert(0, [0] * n)
# a.append([0] * n)
#
# for x in a:
#     x.insert(0, 0)
#     x.append(0)
#
# cnt = 0
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]
#
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         # a[0][1] a[1][2] a[2][1] a[1][0]
#         # 봉우리(a[i][j])가 감싸고 있는 지역(a[i + dx[k]][j+dy[k]])보다 높으면 cnt += 1
#         if all(a[i][j] > a[i + dx[k]][j+dy[k]] for k in range(4)):
#             cnt += 1
#
# print(cnt)


'''
5
5 3 7 2 3
3 7 1 6 1
7 2 5 3 4
4 3 6 4 1
8 7 3 5 2
'''

# 복습

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

arr.insert(0, [0] * n)
arr.append([0] * n)

for x in arr:
    x.insert(0, 0)
    x.append(0)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cnt = 0

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if all(arr[i][j] > arr[i + dx[x]][j + dy[x]] for x in range(4)):
            cnt += 1

print(cnt)