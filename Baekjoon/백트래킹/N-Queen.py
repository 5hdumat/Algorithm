def set(i: int) -> None:
    global res

    for j in range(n):
        if flag[j] == 0 and flag2[i + j] == 0 and flag3[i - j + (n - 1)] == 0:
            if i == (n - 1):
                res += 1

            else:
                flag[j] = flag2[i + j] = flag3[i - j + (n - 1)] = 1
                set(i + 1)
                flag[j] = flag2[i + j] = flag3[i - j + (n - 1)] = 0


n = int(input())

flag = [0] * n
flag2 = [0] * (n * 2 - 1)
flag3 = [0] * (n * 2 - 1)
res = 0
set(0)

print(res)
