# https://www.acmicpc.net/problem/1966

test_case = int(input())

for _ in range(test_case):
    n, m = map(int, input().split())
    imp = list(map(int, input().split()))
    temp = list(range(n))
    temp[m] = 't'
    
    order = 0
    while (True):
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