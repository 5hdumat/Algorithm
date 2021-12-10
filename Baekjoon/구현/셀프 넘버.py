# https://www.acmicpc.net/problem/4673

num_list = list(range(1, 10001))
construct_num = []

for i in num_list: # 1부터 10000 범위 리스트 반복문에서 519 일 경우
    for j in str(i): # 519를 5, 1, 9로 나눠 반복문 생성
        i += int(j) # 519 + 5 + 1 + 9 는 생성자가 있는 수 이므로 이므로
    
    construct_num.append(i) # construct_num에 append

# 셀프 넘버 출력
# 리스트 끼리 빼기 연산자가 실행되지 않기 때문에 set으로 형변환 후 sorted하여 정렬과 리스트 형변환을 동시에 한다.
for i in sorted(set(num_list) - set(construct_num)):
    print(i)