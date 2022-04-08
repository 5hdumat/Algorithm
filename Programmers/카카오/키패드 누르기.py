def solution(numbers, hand):
    answer = ''

    # x, y축으로 생각해보자.
    keypad = {
        1: [0, 0], 2: [1, 0], 3: [2, 0],
        4: [0, 1], 5: [1, 1], 6: [2, 1],
        7: [0, 2], 8: [1, 2], 9: [2, 2],
        '*': [0, 3], 0: [1, 3], '#': [2, 3]
    }

    hand = 'L' if hand == 'left' else 'R'

    cur_left = '*'
    cur_right = '#'
    for x in numbers:
        if keypad[x][0] == 0:
            answer += 'L'
            cur_left = x

        elif keypad[x][0] == 2:
            answer += 'R'
            cur_right = x

        else:
            answer += get_distance(cur_left, cur_right, hand, keypad, x)

            if answer[-1] == 'L':
                cur_left = x
            else:
                cur_right = x

    return answer


def get_distance(cur_left, cur_right, hand, keypad, x):
    left = abs(keypad[x][0] - keypad[cur_left][0]) + abs(keypad[x][1] - keypad[cur_left][1])
    right = abs(keypad[x][0] - keypad[cur_right][0]) + abs(keypad[x][1] - keypad[cur_right][1])

    if left == right:
        return hand

    return 'L' if left < right else 'R'


solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right")
