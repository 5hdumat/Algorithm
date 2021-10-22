'''
1 4 3 6 2 8 5 7 9
5 7 2 1 3 9 4 6 8
9 8 6 7 5 4 2 3 1
3 9 1 5 4 2 7 8 6
4 6 8 9 1 7 3 5 2
7 2 5 8 6 3 9 1 4
2 3 7 4 8 1 6 9 5
6 1 9 2 7 5 8 4 3
8 5 4 3 9 6 1 2 7
'''

# 내 문제 풀이
def check(a):
    for i in range(9):
        check1 = [0] * 10  # 행
        check2 = [0] * 10  # 열

        for j in range(9):
            check1[a[i][j]] = 1
            check2[a[j][i]] = 1

        if sum(check1) != 9 or sum(check2) != 9:
            return False

    dx = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
    for i in range(1, 9, 3):
        for j in range(1, 9, 3):
            check3 = [0] * 10  # 격자

            for k in range(9):
                check3[a[i + dx[k]][j + dy[k]]] = 1

            if sum(check3) != 9:
                return False

    return True

a = [list(map(int, input().split())) for _ in range(9)]
if check(a):
    print("YES")
else:
    print("NO")

# 강의 문제 풀이
def check(a):
    for i in range(9):
        check1 = [0] * 10  # 행
        check2 = [0] * 10  # 열

        for j in range(9):
            check1[a[i][j]] = 1
            check2[a[j][i]] = 1

        if sum(check1) != 9 or sum(check2) != 9:
            return False

    for i in range(3):
        for j in range(3):
            check3 = [0] * 10  # 격자

            for k in range(3):
                for s in range(3):
                    check3[a[i*3+k][j*3+s]] = 1

            if sum(check3) != 9:
                return False

    return True

a = [list(map(int, input().split())) for _ in range(9)]
if check(a):
    print("YES")
else:
    print("NO")
