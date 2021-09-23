'''
리스트와 내장함수 (1)
'''

# 리스트 선언 방법
a = []
a = list()
a = [1, 2, 3, 4, 5]

print(a)  # [1, 2, 3, 4, 5]
print(a[0])  # 1

# range로 리스트 초기화 하기
b = list(range(1, 10))
print(b)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 리스트 합치기
c = a + b
print(c)  # [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 배열에 값 추가하기
a.append(6)
print(a)  # [1, 2, 3, 4, 5, 6]

# 특정 인덱스 지점에 값 추가하기
a.insert(3, 7)  # 3번 인덱스에 7추가하기
print(a)  # [1, 2, 3, 7, 4, 5, 6]

# 리스트에서 맨 뒤에 있는 값 제거
a.pop()
print(a)  # [1, 2, 3, 7, 4, 5]

# 특정 인덱스 값 제거
a.pop(3)
print(a)  # [1, 2, 3, 4, 5]

# 특정 값 찾아서 제거
a.remove(4)
print(a)  # [1, 2, 3, 5]

# 특정 값으로 인덱스 값 찾기
print(a.index(5))  # 5라는 값을 3번 인덱스에 있으니 3

a = list(range(1, 11))
print(a)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 리스트에 있는 모든 값의 합
print(sum(a))  # 55

# 리스트에서 가장 큰 값 찾기
print(max(a))  # 10

# 리스트에서 가장 작은 값 찾기
print(min(a))  # 1

# min, max는 인자값으로 비교함
print(min(7, 3, 5))  # 3

# 리스트 값 섞기
import random as r

r.shuffle(a)
print(a)

# 내림차순 정렬
a.sort(reverse=True)
print(a)

# 오름차순 정렬
a.sort()
print(a)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 리스트 지우기
a.clear()
print(a)  # []
