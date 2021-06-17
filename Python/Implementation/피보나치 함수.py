# https://www.acmicpc.net/problem/1003

# 비효율적인 재귀 연산으로 인한 시간초과 발생
import sys

test_case = int(sys.stdin.readline())

def fibonacci(n):
    if n == 0:
        temp[0] += 1
        return
    elif n == 1:
        temp[1] += 1
        return
    else:
        fibonacci(n-1)
        fibonacci(n-2)
        return 

for _ in range(test_case):
    n = int(sys.stdin.readline())
    temp = [0, 0]
    
    fibonacci(n)
    
    print(*temp)
    
    
# 최종 문제해결
import sys

test_case = int(input())

zero = [1, 0]
one = [0, 1]

def fibonacci(n):
    if n >= 2:
        for i in range(len(zero), n+1):
            zero.append(zero[i-1] + zero[i-2])
            one.append(one[i-1] + one[i-2])
        
    print("%d %d" % (zero[n], one[n]))
    
for _ in range(test_case):
    n = int(sys.stdin.readline())
    
    fibonacci(n)
    
    
