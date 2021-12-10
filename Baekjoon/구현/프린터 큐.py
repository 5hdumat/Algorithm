# https://www.acmicpc.net/problem/1966
import sys

test_case = int(sys.stdin.readline())

for _ in range(test_case):
    n, m = map(int, sys.stdin.readline().split())
    imp = list(map(int, sys.stdin.readline().split()))
    temp = list(range(n))
    temp[m] = 't'
    
    order = 0
    while True:
        if imp[0] == max(imp):
            order += 1
            
            if temp[0] == 't':
                print(order)
                break
            else:
                imp.pop(0)
                temp.pop(0)
        else:
            imp.append(imp.pop(0))
            temp.append(temp.pop(0))