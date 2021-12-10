arr = [5, 3, 7, 9, 2, 5, 2, 6]

# 문제 풀이 1
arrMin = float("inf") # 파이썬에서 가장 큰 값으로 초기화

for i in range(len(arr)):
    if arr[i] < arrMin:
        arrMin = arr[i]

print(arrMin)

# 문제 풀이 2
arrMin = arr[0]
for x in arr:
    if x < arrMin:
        arrMin = x

print(arrMin)


