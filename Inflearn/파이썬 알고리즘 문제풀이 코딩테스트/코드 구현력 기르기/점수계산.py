# 내 문제풀이
# 10
# 1 0 1 1 1 0 0 1 1 0

n = int(input())
answers = list(map(int, input().split()))
tmp = []
result = 0

for answer in answers:
    if answer:
        tmp.append(answer)
        result += len(tmp)
    else:
        tmp = []

print(result)

# 강의 문제 풀이
n = list(input())
a = list(map(int, input().split()))
sum = 0
cnt = 0

for x in a:
    if x == 1:
        cnt += 1
        sum += cnt
    else:
        cnt = 0

print(sum)
