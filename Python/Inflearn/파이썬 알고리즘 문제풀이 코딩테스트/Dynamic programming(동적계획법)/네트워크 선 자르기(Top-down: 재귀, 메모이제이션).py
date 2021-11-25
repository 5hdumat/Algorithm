def DFS(len):
    # dy에 값이 이미 있다면 따로 구하지말고 그대로 리턴
    if dy[len] > 0:
        return dy[len]

    if len == 1 or len == 2:
        dy[len] = len
        return len

    else:
        dy[len] = DFS(len-1) + DFS(len-2)
        return dy[len]

n = int(input())
dy = [0] * (n + 1)
print(DFS(n))
