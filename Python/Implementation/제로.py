# https://www.acmicpc.net/problem/10773

k = int(input())
book = []

for _ in range(k):
    number = int(input())
    
    if number == 0:
        book.pop()
    else:
        book.append(number)
        
print(sum(book))
    