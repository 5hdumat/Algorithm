# https://www.acmicpc.net/problem/1929
m, n = map(int, input().split())

prime_check = [True] * (n+1)
prime_number = []

for i in range(2, n+1):
    if prime_check[i]:
        prime_number.append(i)
        for j in range(i*2, n+1, i):
            prime_check[j] = False
 
# 시간: 512 ms     
print(*list(filter(lambda x : x >= m, prime_number)), sep='\n')

# 시간: 464 ms
for i in prime_number:
    if i >= m:
        print(i)