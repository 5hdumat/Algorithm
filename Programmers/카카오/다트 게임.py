def solution(dartResult):
    answer = []
    dartResult = dartResult.replace('10', 'k')
    point = ['10' if x == 'k' else x for x in dartResult]
    sdt = ['S', 'D', 'T']

    for x in point:
        if x.isdigit():
            answer.append(int(x))
            continue

        if x in sdt:
            answer.append(answer.pop() ** (sdt.index(x) + 1))

        elif x == '*':
            tmp = answer.pop() * 2

            if len(answer) >= 1:
                answer.append(answer.pop() * 2)

            answer.append(tmp)

        elif x == '#':
            answer.append(answer.pop() * -1)

    return sum(answer)


# 1^2 * (-1) * 2 + 2^1 * 2 + 3^1
# solution("1D#2S*3S")
solution("1D2S#10S")
# solution("1D2S0T")
# solution("1T2D3D#")
# solution("1D#2S*3S")
# solution("1S*2T*3S")
# solution("1D2S3T*")
