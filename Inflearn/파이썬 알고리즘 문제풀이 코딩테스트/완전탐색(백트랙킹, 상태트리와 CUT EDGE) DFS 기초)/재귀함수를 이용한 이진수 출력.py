def trans_binary(n):
    a = n // 2  # 나누기 후 소수점 이하의 수는 버리고 정수만 출력
    b = n % 2

    res.insert(0, b)

    if a != 0:
        trans_binary(a)


res = []
trans_binary(int(input()))

print(''.join([str(x) for x in res]))


# 강의 문제 풀이
def dfs(x):
    if x == 0:
        return  # 리턴만 쓰면 함수를 종료하라는 의미가 되기도 함
    else:
        dfs(x // 2)
        print(x % 2, end='')


if __name__ == "__main__":
    n = int(input())
    dfs(n)


# 복습

def DFS(x):
    if x == 0:
        return
    else:
        DFS(x // 2)
        print(x % 2, end='')


n = int(input())
DFS(n)
