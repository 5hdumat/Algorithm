# 내 문제풀이
n = int(input())
is_prime = [True] * (n + 1)

for i in range(2, n + 1):
    if is_prime[i]:
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False

print(is_prime.count(True) - 2)

# 강의 문제 풀이

n = int(input())
ch = [0] * (n + 1)
cnt = 0

for i in range(2, n+1):
    if ch[i] == 0:
        cnt += 1
        for j in range(i, n+1, i):
            ch[j] = 1

print(cnt)