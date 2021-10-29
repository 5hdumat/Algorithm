'''
8
5 3 4 0 2 1 1 0
'''
n = int(input())
a = list(map(int, input().split()))

a = a[::-1]
res = []
for x in a:
    res.insert(x, n)
    n -= 1

print(*res)

n = int(input())
a = list(map(int, input().split()))
a.insert(0, 0)
seq = [0] * n
for i in range(1, n + 1):
    for j in range(n):
        if a[i] == 0 and seq[j] == 0:
            seq[j] = i
            break
        elif seq[j] == 0:
            a[i] -= 1

print(*seq)
