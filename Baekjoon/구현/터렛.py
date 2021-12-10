# https://www.acmicpc.net/problem/1002
# - 문제의 목표는?
#   - 두 터렛 사이의 거리를 알기 위해 원의 방정식을 이해한다.  
#       - (x1-x2)**2 + (y1-y2)**2 = r**2
#   - 원이 접점을 일으키는 경우의 수를 알 수 있다.
#       -1 : 두 원이 일치하는 경우 :: r==0 and r1==r2
#       1 : 두 원이 한 점에서 만나는 경우 (외접, 내접) :: r == r1 + r2 혹은 r, r1, r2 중 가장 긴 값이 나머지 두 값의 합과 같은 경우
#       0 : 두 원이 만나지 않는 경우 :: r, r1, r2 중 가장 긴 값이 나머지 두 값의 합보다 큰 경우
#       2 : 두 원이 두 점에서 만나는 경우 :: 위 세 가지 경우 외 모두

import sys

test_case = int(input())

for _ in range(test_case):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    
    r = ((x1-x2)**2 + (y1-y2)**2)**(1/2) # 제곱근을 연산하고 싶은 값을 입력하고** (제곱을 수행한 후) (1/2)의 값을 곱한다.
    
    tmp = [r1, r2, r]
    max_r = max(tmp)
    
    tmp.remove(max_r)
    remainder = sum(tmp)
    
    if r == 0 and r1 == r2: # 두 원이 일치하는 경우
        print(-1)
    elif r == r1 + r2 or max_r == remainder: # 두 원이 한 점에서 만나는 경우 (외접, 내접)
        print(1)
    elif max_r > remainder: # 두 원이 만나지 않는 경우
        print(0)
    else:
        print(2)
    
    
    