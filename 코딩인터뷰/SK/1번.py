def solution(money, costs):
    tmp = []

    for i, v in enumerate([1, 5, 10, 50, 100, 500]):
        tmp.append((v / costs[i], costs[i], v))

    tmp.sort(reverse=True)

    # print(tmp)
    answer = 0
    for x in tmp:
        while True:
            # print(x)
            money -= x[2]
            answer += x[1]

            if money < 0:
                money += x[2]
                answer -= x[1]
                break

        if not money:
            return answer

    return answer


solution(4578, [1, 4, 99, 35, 50, 1000])
# solution(1999, [2, 11, 20, 100, 200, 600])
# solution(1000000, [2, 11, 2, 100, 200, 600])
