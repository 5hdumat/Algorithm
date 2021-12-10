'''
10 3
13 15 34 23 45 65 33 11 26 42
'''
# 내 문제 풀이
n, m = map(int, input().split())
number_list = list(map(int, input().split()))
res = set()

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            res.add(number_list[i] + number_list[j] + number_list[k])

res = list(res)
res.sort(reverse=True)

print(res[m - 1])

# 강의 문제풀이

n, k = map(int, input().split())
a = list(map(int, input().split()))
res = set()

for i in range(n):
    for j in range(i + 1, n):
        for m in range(j + 1, n):
            res.add(a[i] + a[j] + a[m])

res = list(res)
res.sort(reverse=True)

print(res[k - 1])

# 복습
n, k = map(int, input().split())
arr = list(map(int, input().split()))
tmp = set()

for i in range(n):
    for j in range(i + 1, n):
        for m in range(j + 1, n):
            tmp.add(arr[i] + arr[j] + arr[m])

tmp = list(tmp)
tmp.sort(reverse=True)
print(tmp[k-1])
