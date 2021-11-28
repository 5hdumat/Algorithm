'''
5
3 7 2 1 9
5 8 3 9 2
5 3 1 2 3
5 4 3 2 1
1 7 5 2 4
'''

# 이건 도착점부터 출발한다.
def DFS(x, y):
    if x == 0 and y == 0:
        return arr[x][y]

    else:
        if y == 0:
            return DFS(x - 1, y) + arr[x][y]

        elif x == 0:
            return DFS(x, y - 1) + arr[x][y]

        else:
            return min(DFS(x-1, y), DFS(x, y-1)) + arr[x][y]


if __name__ == "__main__":
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    print(DFS(n - 1, n - 1))
