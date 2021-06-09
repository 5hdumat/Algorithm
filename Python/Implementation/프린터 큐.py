# https://www.acmicpc.net/problem/1966

test_case = int(input())

for _ in range(test_case):
    n, m = map(int, input().split()) 
    imp = list(map(int, input().split())) # 중요도
    idx = [i+1 for i in range(n)]
    idx[m] = 't' # 타겟
    
    position = 0
    
    while(True):
        if imp[0] == max(imp):
            position += 1

            if idx[0] == 't':
                print(position)
                break
            
            else: #출력
                imp.pop(0)
                idx.pop(0)
                
        else:
            imp.append(imp.pop(0))
            idx.append(idx.pop(0))
        