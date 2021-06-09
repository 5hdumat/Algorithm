# https://www.acmicpc.net/problem/1966

test_case = int(input())

# _ : 인덱스 무시
for _ in range(test_case):
    n, m = map(int, input().split()) # 6 1
    importance = list(map(int, input().split())) # [1 1 9 1 2 3]
    idx = list(range(len(importance))) # [1, 2, 3, 4, 5, 6]
    idx[m] = "target" # [1, target, 3, 4, 5, 6]
    
    order = 0
    
    while(True):
        if importance[0] == max(importance): 
            order += 1
            
            if idx[0] == "target":
                print(order)
                break
            else:
                importance.pop(0) # 출력한다고 생각
                idx.pop(0) 
        
        else:
            importance.append(importance.pop(0)) # 191231 912311 12311
            idx.append(idx.pop(0)) # target34561 34561target 4561target