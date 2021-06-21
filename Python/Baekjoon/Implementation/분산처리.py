# https://www.acmicpc.net/problem/1009

import sys 

test_case = int(input())

for _ in range(test_case):
    a, b = map(int, sys.stdin.readline().split())
    data_cnt = a ** b
    
    print(data_cnt % 10)
