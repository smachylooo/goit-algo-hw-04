import random
import timeit

def insertion_sort(arr):
    arr = arr.copy()

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

data_small = [random.randint(1, 1000) for _ in range(100)]
data_medium = [random.randint(1, 1000) for _ in range(1000)]
data_large = [random.randint(1, 1000) for _ in range(5000)]

def test_sorting():
    print("SMALL ARRAY")
    print(
        "Insertion Sort:",
        timeit.timeit(lambda: insertion_sort(data_small), number=10)
    )
    print(
        "Merge Sort:",
        timeit.timeit(lambda: merge_sort(data_small), number=10)
    )
    print(
        "Timsort:",
        timeit.timeit(lambda: sorted(data_small), number=10)
    )
    print("\nMEDIUM ARRAY")
    print(
        "Insertion Sort:",
        timeit.timeit(lambda: insertion_sort(data_medium), number=10)
    )
    print(
        "Merge Sort:",
        timeit.timeit(lambda: merge_sort(data_medium), number=10)
    )
    print(
        "Timsort:",
        timeit.timeit(lambda: sorted(data_medium), number=10)
    )
    print("\nLARGE ARRAY")
    print(
        "Insertion Sort:",
        timeit.timeit(lambda: insertion_sort(data_large), number=10)
    )
    print(
        "Merge Sort:",
        timeit.timeit(lambda: merge_sort(data_large), number=10)
    )
    print(
        "Timsort:",
        timeit.timeit(lambda: sorted(data_large), number=10)
    )

test_sorting()