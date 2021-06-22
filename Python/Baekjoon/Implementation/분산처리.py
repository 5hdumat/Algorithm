# https://www.acmicpc.net/problem/1009

# 시간초과 + 일의 자리가 0일때 10으로 출력 안돼서 틀림
# import sys 

# test_case = int(input())

# for _ in range(test_case):
#     a, b = map(int, sys.stdin.readline().split())
#     data_cnt = a ** b
    
#     print(data_cnt % 10)

# 문제풀이
# 제곱 후 1 의 자리 숫자
# 0 : 0 (print 10)
# 1 : 1
# 2 : 2 4 8 6 (반복)
# 3 : 3 9 7 1 (반복)
# 4 : 4 6 (반복)
# 5 : 5 (반복)
# 6 : 6 (반복)
# 7 : 7 9 3 1 (반복)
# 8 : 8 4 2 6 (반복)
# 9 : 9 1 (반복)
import sys

array1 = []
array2 = []
test_case = int(input())

output = []
for _ in range(test_case):
    a, b = map(int, sys.stdin.readline().split())
    
    array1.append(int(a))
    array2.append(int(b))
    
for x in range(test_case):
    result = array1[x] % 10 
    
    if result == 0:
        print(10)
        
    elif result in [1, 5 ,6]:
        print(result)
        
    elif result in [4, 9]:
        if array2[x] % 2 == 0:
            print((result ** 2) % 10)
        else:
            print(result)
            
    else: # 지수 값 2, 3, 7, 8
        if array2[x] % 4 == 0:
            print(result ** 4 % 10)
        else:
            print(result ** (array2[x] % 4) % 10)
    
    