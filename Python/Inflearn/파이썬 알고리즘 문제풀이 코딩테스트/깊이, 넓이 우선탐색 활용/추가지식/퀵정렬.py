def Qsort(lt, rt):
    if lt < rt:
        pos = lt
        pivot = arr[rt]

        for i in range(lt, rt):
            if arr[i] <= pivot:
                arr[i], arr[pos] = arr[pos], arr[i]
                pos += 1

        arr[pos], arr[rt] = arr[rt], arr[pos]

        Qsort(lt, pos - 1)
        Qsort(pos + 1, rt)


if __name__ == "__main__":
    arr = [21, 45, 23, 36, 15, 67, 11, 60, 20, 33]
    Qsort(0, len(arr) - 1)
    print(arr)
