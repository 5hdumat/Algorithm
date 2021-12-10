# https://www.acmicpc.net/problem/1475

n = input()
number_list = [0] * 10

for i in range(len(n)):
    num = int(n[i])
    
    if num == 9 or num == 6:
        if number_list[9] >= number_list[6]:
            number_list[6] += 1
        elif number_list[9] <= number_list[6]:
            number_list[9] += 1
    else:
        number_list[num] += 1
    
print(max(number_list))