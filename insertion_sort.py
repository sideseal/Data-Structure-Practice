def insertion_sort1(arr):
    for end in range(1, len(arr)):
        for i in range(end, 0, -1):
            if arr[i-1] > arr[i]:
                arr[i-1], arr[i] = arr[i], arr[i-1]


def insertion_sort2(arr):
    for end in range(1, len(arr)):
        i = end
        while i > 0 and arr[i-1] > arr[i]:
            arr[i-1], arr[i] = arr[i], arr[i-1]
            i -= 1


def insertion_sort3(arr):
    for end in range(1, len(arr)):
        to_insert = arr[end]
        i = end
        while i > 0 and arr[i-1] > to_insert:
            arr[i] = arr[i-1]
            i -= 1
        arr[i] = to_insert
