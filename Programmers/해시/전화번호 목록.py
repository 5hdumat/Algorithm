def solution(phone_book):
    answer = True

    # 해시는 해시답게 풀어야지!
    hash_map = {}

    for phone_number in phone_book:
        hash_map[phone_number] = hash_map.get(phone_number, 0) + 1

    for phone_number in phone_book:
        tmp = ""

        for number in phone_number:
            tmp += number

            if tmp in hash_map and tmp != phone_number:
                return False

    # 파이썬 내장 함수를 써보자 (zip, startswith)
    phone_book.sort()

    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False

    # 그냥 풀어보자

    phone_book.sort()

    for i in range(len(phone_book) - 1):
        if phone_book[i] in phone_book[i + 1][:len(phone_book[i])]:
            return False

    return answer