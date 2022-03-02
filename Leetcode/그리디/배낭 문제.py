'''
배낭에 담을 수 있는 무게의 최댓값이 정해져 있고, 각각 짐의 가치와 무게가 있는 짐들을 배낭에 넣었을 때 가치의 합이 최대가 되도록 짐을 고르시오.
'''


# 1. 배낭에는 15kg의 짐이 들어간다.
# 2. 짐의 가치, 무게는 아래와 같다.
# cargo = [
#     (4, 12),
#     (2, 1),
#     (10, 4),
#     (1, 1),
#     (2, 2)
# ]


def greedy(cargo, capacity):
    tmp = []
    for x in cargo:
        # (키로 당 짐의가치, 가치, 무게)
        tmp.append((x[0] / x[1], x[0], x[1]))

    tmp.sort(reverse=True)

    max_value: float = 0
    for x in tmp:
        if capacity - x[2] >= 0:
            capacity -= x[2]
            max_value += x[1]
        else:
            max_value += (capacity / x[2]) * x[1]
            break

    return round(max_value, 1)


print(greedy([(4, 12), (2, 1), (10, 4), (1, 1), (2, 2)], 15))
