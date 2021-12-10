# 풀이 1
def dfs(l):
    global cnt

    if l == m:
        print(*res)
        cnt += 1
        return
    else:
        for i in range(1, n + 1):
            if ch[i] == 0:
                ch[i] = 1
                res[l] = i
                dfs(l + 1)
                ch[i] = 0


if __name__ == "__main__":
    n, m = map(int, input().split())
    res = [0] * m
    ch = [0] * (n + 1)
    cnt = 0
    dfs(0)
    print(cnt)



# 강의 문제 풀이

def dfs(l):
    global cnt

    if l == m:
        for j in range(l):
            print(res[j], end=' ')
        print()
        cnt += 1
    else:
        for i in range(1, n + 1):
            if ch[i] == 0:
                ch[i] = 1
                res[l] = i

                dfs(l+1)

                ch[i] = 0

if __name__ == "__main__":
    n, m = map(int, input().split())
    res = [0] * n
    ch = [0] * (n + 1)
    cnt = 0
    dfs(0)
