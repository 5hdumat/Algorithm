def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        tmp = ''
        for x in bin(arr1[i] | arr2[i])[2:].zfill(n):
            if x == '1':
                tmp += '#'
            else:
                tmp += ' '

        answer.append(tmp)

    return answer


# solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28])
solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10])
