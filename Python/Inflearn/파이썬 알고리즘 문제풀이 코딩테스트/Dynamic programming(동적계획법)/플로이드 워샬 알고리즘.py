'''
5 8
1 2 6
1 3 3
3 2 2
2 4 1
2 5 13
3 4 5
4 2 3
4 5 7
'''

if __name__ == "__main__":
    n, m = map(int, input().split())

    # 갈 수 없는 영역은 9999로 표현
    dy = [[9999] * (n + 1) for _ in range(n + 1)]

    # 자기자신에서 자기자신으로 가는 것은 비용을 0으로 환산
    for i in range(n + 1):
        dy[i][i] = 0

    # 직행하는 노드 경로
    for i in range(m):
        a, b, c = map(int, input().split())
        dy[a][b] = c

    # 최단 경로 찾아서 다이나믹 테이블 수정
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                dy[i][j] = min(dy[i][j], dy[i][k] + dy[k][j])

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if dy[i][j] == 9999:
                print('M', end=' ')
            else:
                print(dy[i][j], end=' ')
        print()
