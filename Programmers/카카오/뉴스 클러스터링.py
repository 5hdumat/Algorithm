import collections


def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()

    tmp1, tmp2 = slicing(str1, str2)

    # 다중 교집합
    inter = sum((collections.Counter(tmp1) & collections.Counter(tmp2)).values())

    # 다중합집합
    union = sum((collections.Counter(tmp1) | collections.Counter(tmp2)).values())

    jaccard = 1 if union == 0 else inter / union
    return int(jaccard * 65536)


def slicing(str1, str2):
    tmp1 = []

    for i in range(len(str1) - 1):
        s = str1[i:i + 2]
        if s.isalpha():
            tmp1.append(s)

    tmp2 = []
    for i in range(len(str2) - 1):
        s = str2[i:i + 2]
        if s.isalpha():
            tmp2.append(s)

    return tmp1, tmp2

# solution("FRANCE", 'french')
# solution("E=M*C^2", 'e=m*c^2')
# solution("aa1+aa2", "aa1+aa2")
# solution("handshake", "shake hands")
