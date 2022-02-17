def bubble_sort(x):
    k = 0
    num = len(x)

    while k < num - 1:
        last = num - 1

        for j in range(num - 1, k, -1):
            if x[j - 1] > x[j]:
                x[j - 1], x[j] = x[j], x[j - 1]
                last = j

        k = last


bubble_sort([1, 3, 4, 5, 2])
