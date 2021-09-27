# 내 문제 풀이
test_case = int(input())
result = []
for _ in range(test_case):
    n, s, e, k = map(int, input().split())
    number_list = list(map(int, input().split()))[s - 1:e]
    number_list.sort()
    result.append(number_list[k - 1])

for index, value in enumerate(result):
    print("#%d %d" % (index+1, value))

# 강의 문제풀이
T = int(input())

for t in range(T):
    n, s, e, k = map(int, input().split())
    a = list(map(int, input().split()))
    a = a[s - 1:e]
    a.sort()
    print(a[k - 1])
    print("#%d %d" % (t+1, a[k - 1]))
