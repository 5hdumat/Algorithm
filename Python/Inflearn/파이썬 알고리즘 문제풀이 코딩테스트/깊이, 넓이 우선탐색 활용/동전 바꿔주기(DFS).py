'''
20
3
5 3
10 2
1 5
'''


def dfs(l, sum):
    global cnt

    if sum > T:
        return

    if l == k:
        if sum == T:
            cnt += 1
            return

    else:
        for i in range(cn[l]+1):
            dfs(l + 1, sum + (cv[l] * i))


T = int(input())
k = int(input())
cv = [] # coin value
cn = [] # coin number

for _ in range(k):
    a, b = map(int, input().split())
    cv.append(a)
    cn.append(b)

cnt = 0

dfs(0, 0)
print(cnt)
