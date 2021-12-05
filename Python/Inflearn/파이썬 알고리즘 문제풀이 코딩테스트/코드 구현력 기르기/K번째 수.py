'''
2
6 2 5 3
5 2 7 3 8 9
15 3 10 3
4 15 8 16 6 6 17 3 10 11 18 7 14 7 15
'''
# 내 문제 풀이
test_case = int(input())
result = []
for _ in range(test_case):
    n, s, e, k = map(int, input().split())
    number_list = list(map(int, input().split()))[s - 1:e]
    number_list.sort()
    result.append(number_list[k - 1])

for index, value in enumerate(result):
    print("#%d %d" % (index + 1, value))

# 강의 문제풀이
T = int(input())

for t in range(T):
    n, s, e, k = map(int, input().split())
    a = list(map(int, input().split()))
    a = a[s - 1:e]
    a.sort()
    print(a[k - 1])
    print("#%d %d" % (t + 1, a[k - 1]))

# 복습
T = int(input())

cnt = 1
for _ in range(T):
    n, s, e, k = map(int, input().split())
    arr = list(map(int, input().split()))

    tmp = arr[s - 1:e]
    tmp.sort()

    print("#%d %d" % (cnt, tmp[k-1]))

    cnt += 1
