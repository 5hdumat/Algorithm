'''
259 5
81
58
42
33
61
'''

# 복습
def DFS(l, sum, total):
    global res

    if sum + (tw - total) < res:
        return

    if sum > c:
        return

    if l >= n:
        if sum > res:
            res = sum

        return

    else:
        DFS(l+1, sum, total + a[l])
        DFS(l+1, sum + a[l], total + a[l])


c, n = map(int, input().split())
a = []
for _ in range(n):
    a.append(int(input()))

tw = sum(a) # total_weight
res = 0
DFS(0, 0, 0)

print(res)