def quick_sort(x, lo, hi):
    def partition(lo, hi):
        pivot = x[hi]
        left = lo

        for right in range(lo, hi):
            if x[right] < pivot:
                x[left], x[right] = x[right], x[left]
                left += 1

        x[left], x[hi] = x[hi], x[left]
        return left

    if lo < hi:
        pivot = partition(lo, hi)
        quick_sort(x, lo, pivot - 1)
        quick_sort(x, pivot + 1, hi)


# 3, 6, 3, 7, 5
# 3, 6, 3, 7, 5
# 3, 3, 6, 7, 5

x = [3, 6, 3, 7, 5]
lo, hi = 0, len(x) - 1
quick_sort(x, lo, hi)
