# https://www.acmicpc.net/problem/1316

import sys

# word_count = int(sys.stdin.readline())

# count = 0
# for _ in range(word_count):
#     word = list(sys.stdin.readline().strip())

#     if len(word) == 1:
#         count += 1
#     else:
#         word_check = []
#         for i in word:
#             if not i in word_check or i == word_check[-1]:
#                 word_check.append(i)
                
#                 if len(word_check) == len(word):
#                     count += 1
            
# print(count)
                    
# 슬라이싱을 이용한 방법
word_count = int(sys.stdin.readline())

count = 0
for _ in range(word_count):
    word = sys.stdin.readline()
    
    for i in range(len(word)-1):
        if word[i] != word[i+1]: # 연속적으로 나열되어있지 않으면서
            if word[i] in word[i+1:]: # 포함관계에 있으면 
                word_count -= 1 # word_count -1
                break
            
print(word_count)
        

